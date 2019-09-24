import tensorflow as tf
from tensorflow import keras

class Downsample(keras.Model):

    def __init__(self, hyperParam):
        super(Downsample, self).__init__()

        self.applyBatchNorm = hyperParam.applyBatchNormalization
        self.numFilter = hyperParam.numFilter
        self.batchSize = hyperParam.batchSize
        self.imageHeight = hyperParam.Height
        self.imageWidth = hyperParam.Width
        self.imageChannels = hyperParam.Channels
        # self.kernelSize = hyperParam.kernelSize
        # self.strides = hyperParam.strides

        initializer = tf.random_normal_initializer(0, 0.02)
        # filter(output dimension)
        # kernel_size(height, width)
        # strides(height, width) dilation!=1
        # padding(valid same)
        # data_format(input shape /channels_last[batch, height, width, channels])
        # /channels_first[batch, channels, height, width] default-channels_last
        # dilation_rate an integer/ 2 integer
        # activation /activation function default(f(x) = x)
        # use_bias(Boolean, whether the layer use a bias vector)
        # kernel_initializer kernel weights matrix
        # bias_initializer initializer for the bias vector
        # kernel_regularizer regularizer function applied to the kernel weights matrix
        # bias_regularizer regularizer function applied to the bias vector
        # activity_regularizer regularizer function applied to the output of the layer(it's activation)
        # kernel_constraint constraint function applied to the kernel matrix
        # bias_constraint constraint function applied to the bias vector

        self.enInput = keras.
        # self.Down_input = keras.layers.conv2d(self.numFilter, [3, 3], 1, )


hyperParam = dict()
hyperParam['applyNormalization'] = True
hyperParam['imageHeight'] = 512
hyperParam['imageWidth'] = 512
hyperParam['imageChannels'] = 3
hyperParam['batchSize'] = 1
hyperParam['numFilter'] = 64
# hyperParam['kernelSize'] = [3, 3]
hyperParam['strides'] = 1
