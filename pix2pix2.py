k# -*- coding: UTF-8 -*-
"""
Arthur: Shilei Fu
Date: 2018.06.07
Aim: SAR2SEG  OPT2SEG
Add: minibatch discrimination + 两个网络同时训练 + 分割图不需要鉴别器
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import os, json
import scipy.misc
from os.path import dirname, join
import cv2
# import imageio
import scipy.io
import random

# 只显示 warning 和 Error
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

EPS = 1e-12
ngf = 16 #卷积核数量
ndf = 16 #输出通道数量


def discrim_conv(batch_input, out_channels, stride):
	padded_input = tf.pad(batch_input, [[0, 0], [1, 1], [1, 1], [0, 0]], mode="CONSTANT") #保持图像尺寸大小
	initializer = tf.truncated_normal_initializer(stddev=0.02) #正态分布随机
	return tf.layers.conv2d(padded_input, out_channels, kernel_size=4, strides=(stride, stride), padding="valid", kernel_initializer=initializer, kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
	#2维卷积

def gen_conv(batch_input, out_channels, k, s):
	initializer = tf.truncated_normal_initializer(stddev=0.02)
	return tf.layers.conv2d(batch_input, out_channels, kernel_size=k, strides=(s, s), padding="same", kernel_initializer=initializer, kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
	#2维卷积

def gen_deconv(batch_input, out_channels, k, s):
	initializer = tf.random_normal_initializer(0, 0.02)
	return tf.layers.conv2d_transpose(batch_input, out_channels, kernel_size=k, strides=(s, s), padding="same", kernel_initializer=initializer, kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
	#2维转置卷积

def lrelu(x, a): #？非负数化
	with tf.name_scope("lrelu"):
		x = tf.identity(x)
		return (0.5 * (1 + a)) * x + (0.5 * (1 - a)) * tf.abs(x)


def batchnorm(inputs): #局部响应归一化层(正态分布)
	return tf.layers.batch_normalization(inputs, axis=3, epsilon=1e-5, momentum=0.1, training=True, gamma_initializer=tf.random_normal_initializer(1.0, 0.02))
	#Accelerating Deep Network Training by Reducing Internal Covariate Shift

def create_encoder(generator_inputs, scope, reuse):
	layers = []

	with tf.variable_scope(scope):
		if reuse is True:
			tf.get_variable_scope().reuse_variables()
		# encoder_1: [batch, 256, 256, in_channels] => [batch, 128, 128, ngf]
		with tf.variable_scope("encoder_1"):
			output = gen_conv(generator_inputs, ngf, 3, 2) #kernel 3*3 strides=2
			output = batchnorm(output)	# added
			layers.append(output)

		layer_specs = [
			ngf * 2,  # encoder_2: [batch, 128, 128, ngf] => [batch, 64, 64, ngf * 2]
			ngf * 4,  # encoder_3: [batch, 64, 64, ngf * 2] => [batch, 32, 32, ngf * 4]
			ngf * 8,  # encoder_4: [batch, 32, 32, ngf * 4] => [batch, 16, 16, ngf * 8]
			ngf * 8,  # encoder_5: [batch, 16, 16, ngf * 8] => [batch, 8, 8, ngf * 8]
		]

		for out_channels in layer_specs:
			with tf.variable_scope("encoder_%d" % (len(layers) + 1)):
				rectified = lrelu(layers[-1], 0.2)
				# [batch, in_height, in_width, in_channels] => [batch, in_height/2, in_width/2, out_channels]
				# 图片尺寸只压缩到8*8
				if (len(layers) + 1) <= 5:
					convolved = gen_conv(rectified, out_channels, 3, 2)
				else:
					convolved = gen_conv(rectified, out_channels, 3, 1)
				output = batchnorm(convolved)
				layers.append(output)

		return layers


def create_decoder(generator_inputs, generator_outputs_channels, scope, reuse):

	# 避免列表传引用
	layers = []
	layers = generator_inputs[:]

	layer_specs = [
		(ngf * 8, 0.0),	 # decoder_5: [batch, 8, 8, ngf * 8 * 2] => [batch, 16, 16, ngf * 8 * 2] (ngf * 8, 0.0),
		(ngf * 4, 0.0),	 # decoder_4: [batch, 16, 16, ngf * 8 * 2] => [batch, 32, 32, ngf * 4 * 2] (ngf * 4, 0.0),
		(ngf * 2, 0.0),	 # decoder_3: [batch, 32, 32, ngf * 4 * 2] => [batch, 64, 64, ngf * 2 * 2]
		(ngf, 0.0),	 # decoder_2: [batch, 64, 64, ngf * 2 * 2] => [batch, 128, 128, ngf * 2]
	]

	with tf.variable_scope(scope):
		if reuse is True:
			tf.get_variable_scope().reuse_variables()

		num_encoder_layers = len(layers)
		for decoder_layer, (out_channels, dropout) in enumerate(layer_specs):
			skip_layer = num_encoder_layers - decoder_layer - 1 #跳层
			with tf.variable_scope("decoder_%d" % (skip_layer + 1)):
				if decoder_layer == 0:
					# first decoder layer doesn't have skip connections
					# since it is directly connected to the skip_layer
					input = layers[-1]
				else:
					input = tf.concat([layers[-1], layers[skip_layer]], axis=3) #连接

				rectified = tf.nn.relu(input)  #隐藏层的实现
				# [batch, in_height, in_width, in_channels] => [batch, in_height*2, in_width*2, out_channels]
				if (skip_layer + 1) >= 6:
					output = gen_deconv(rectified, out_channels, 3, 1)
				else:
					output = gen_deconv(rectified, out_channels, 3, 2)
				output = batchnorm(output)

				if dropout > 0.0:
					output = tf.nn.dropout(output, keep_prob=1 - dropout) #训练样本丰富（节点数据丢弃）

				layers.append(output)

		# decoder_1: [batch, 128, 128, ngf * 2] => [batch, 256, 256, generator_outputs_channels]
		with tf.variable_scope("decoder_1"):
			input = tf.concat([layers[-1], layers[0]], axis=3)	#连接
			rectified = tf.nn.relu(input)
			output = gen_deconv(rectified, generator_outputs_channels, 3, 2)
			output = tf.tanh(output)
			output = tf.image.resize_bilinear(output, (256, 256), align_corners=True, name = None)
			layers.append(output)

		return layers[-1]


def create_discriminator(discrim_targets, scope, reuse):
	n_layers = 3
	layers = []

	with tf.variable_scope(scope):
		if reuse is True:
			tf.get_variable_scope().reuse_variables()

		# 2x [batch, height, width, in_channels] => [batch, height, width, in_channels * 2]
		# input = tf.concat([discrim_inputs, discrim_targets], axis=3)
		input = discrim_targets

		# layer_1: [batch, 256, 256, in_channels * 2] => [batch, 128, 128, ndf]
		with tf.variable_scope("layer_1"):
			convolved = discrim_conv(input, ndf, stride=2) #分割
			# normalized = batchnorm(convolved)	 # added
			# rectified = lrelu(normalized, 0.2)  # added
			rectified = lrelu(convolved, 0.2)
			layers.append(rectified)

		# layer_2: [batch, 128, 128, ndf] => [batch, 64, 64, ndf * 2]
		# layer_3: [batch, 64, 64, ndf * 2] => [batch, 32, 32, ndf * 4]
		# layer_4: [batch, 32, 32, ndf * 4] => [batch, 31, 31, ndf * 8]
		for i in range(n_layers):
			with tf.variable_scope("layer_%d" % (len(layers) + 1)):
				out_channels = ndf * min(2**(i+1), 8)
				stride = 1 if i == n_layers - 1 else 2	# last layer here has stride 1
				convolved = discrim_conv(layers[-1], out_channels, stride=stride)
				normalized = batchnorm(convolved)
				rectified = lrelu(normalized, 0.2)
				layers.append(rectified)

		# layer_5: [batch, 31, 31, ndf * 8] => [batch, 30, 30, 1]
		with tf.variable_scope("layer_%d" % (len(layers) + 1)):
			convolved = discrim_conv(rectified, out_channels=1, stride=1)
			output = tf.sigmoid(convolved)
			layers.append(output)

		return layers[-1]


class create_model(object): 

	def __init__(self, param): #初始化
		self.l1_weight = param['l1_weight']
		self.gan_weight = param['gan_weight']
		self.IMG_WIDTH = param['IMG_WIDTH']
		self.IMG_HEIGHT = param['IMG_HEIGHT']
		self.IMG_CHANNELS = param['IMG_CHANNELS']
		self._base_lr = param['base_lr']
		self.beta1 = param['beta1']
		self.batch_size = param['batch_size']
		self._max_step = 106
		self._save_every_iterations = 353
		self.LAMBDA = 10.0

	def model_setup(self): #输入数据（格式）
		self.input_a = tf.placeholder(
			tf.float32, [
				1,
				self.IMG_HEIGHT,
				self.IMG_WIDTH,
				self.IMG_CHANNELS, #维度
			], name="input_A")

		self.input_b = tf.placeholder(
			tf.float32, [
				1,
				self.IMG_HEIGHT,
				self.IMG_WIDTH,
				self.IMG_CHANNELS, #维度
			], name="input_B")

		self.learning_rate1 = tf.placeholder(tf.float32, shape=[], name="lr")
		self.learning_rate2 = tf.placeholder(tf.float32, shape=[], name="lr") #学习速率 自己调试复杂/自适应（Adagrad\Adam\Adadelta） SGD的参数（学习速率、Momentum、Nesterov等）
		#开始训练时，学习速率大加速收敛，训练后期速率小稳定落入一个局部最优
	
	 #损失函数定义
	def compute_loss(self):
		with tf.variable_scope("generator"):
			# self.fake_b, self.real_latent = create_generator(self.input_a, self.IMG_CHANNELS)
			self.tmp_a = create_encoder(self.input_b, scope='Encoder1', reuse=False)

			self.fake_a = create_decoder(self.tmp_a, self.IMG_CHANNELS, scope='Decoder1', reuse=False) 

		with tf.name_scope("generator_loss"):
			# self.gen_loss_GAN = tf.reduce_mean(-tf.log(self.predict_fake_a + EPS))

			self.gen_loss_fake = tf.reduce_mean(tf.abs(self.input_a - self.fake_a))

			self.gen_loss = self.gen_loss_fake 
	
	def train(self):
		self.model_setup()
		self.compute_loss()

		init = (tf.global_variables_initializer(), tf.local_variables_initializer()) #全局,本地参数初始化
		saver = tf.train.Saver() 

		with tf.Session() as sess:
			sess.run(init)

			# ckpt = tf.train.get_checkpoint_state('./SAR_test')
			# if ckpt:
				  # saver.restore(sess, ckpt.model_checkpoint_path)
				  # print('loaded ' + ckpt.model_checkpoint_path)

			if not os.path.isdir("./SAR_test"):
				os.makedirs("./SAR_test")

			for epoch in range(0, self._max_step): #轮数迭代
				if os.path.isdir("./SAR_test/%.4d" % epoch):
					continue
				print("In the epoch {}".format(epoch))

				se = np.random.permutation(self._save_every_iterations) + 1
				for i in range(0, self._save_every_iterations):
					print("Processing batch {}/{}".format(i, self._save_every_iterations))

					curr_lr = self._base_lr 

					image_real = np.expand_dims(np.float32(scipy.misc.imread("./mask_samples1/%.4d.bmp" % se[i])), axis=0) / 127.5 - 1
					image_sar = np.expand_dims(np.float32(scipy.misc.imread("./test_samples/%.4d.tiff" % se[i])), axis=0) / 127.5 - 1
					image_real.shape = -1, self.IMG_HEIGHT, self.IMG_WIDTH, 1
					image_sar.shape = -1, self.IMG_HEIGHT, self.IMG_WIDTH, 1
	

				saver.save(sess, "./SAR_test/model.ckpt")

				if not os.path.exists("./SAR_test/%.4d" % epoch):
					os.makedirs("./SAR_test/%.4d" % epoch)

				if epoch >= 2:
					if not os.path.exists("./SAR_test/%.4d/data.mat" % (epoch-2)):
						os.remove("./SAR_test/%.4d/data.mat" % (epoch-2))

				# test
				data = np.zeros((7, self.IMG_HEIGHT, self.IMG_WIDTH, self.IMG_CHANNELS), dtype=np.float32)
				index = 347	 # 测试起始位置序号
				for i in range(index, index+7):
					image_sar = np.expand_dims(np.float32(scipy.misc.imread("./test_samples/%.4d.tiff" % i)), axis=0) / 127.5 - 1
					image_sar.shape = -1, self.IMG_HEIGHT, self.IMG_WIDTH, 1

					fake_temp = sess.run(self.fake_a, feed_dict={self.input_b: image_sar})
					tmp = fake_temp[0]
					tmp = np.where(tmp >0, tmp, 0)
					tmp = np.where(tmp <= 0, tmp, 255)

					data[i - index, :, :, :] = tmp
				scipy.io.savemat('./SAR_test/%.4d/data.mat' % epoch, {'data': data})
			
	


def main():
	with tf.name_scope('SAR_test'):
		param = dict()
		param['l1_weight'] = 100.0
		param['gan_weight'] = 5.0
		param['beta1'] = 0.5
		param['batch_size'] = 1
		param['IMG_WIDTH'] = 256
		param['IMG_HEIGHT'] = 256
		param['IMG_CHANNELS'] = 1
		param['base_lr'] = 0.0001

		model = create_model(param)
		model.train() 


if __name__ == '__main__':
	main()

