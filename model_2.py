import tensorflow as tf
from tensorflow import keras

numFilter = 64
l1_weight = 0.01
drop_rate = 0.3


def bca(num_filters):
    initializer = tf.random_normal_initializer(0, 0.02)
    regularizer = keras.regularizers.l1(l1_weight)
    batch_normal = keras.layers.BatchNormalization(axis=1, momentum=0.1, epsilon=1e-12,
                                                   gamma_initializer=tf.random_normal_initializer(1.0, 0.02))
    normal_conv = keras.layers.Conv2D(num_filters, 3, 1, padding='same', activation='relu',
                                      kernel_initializer=initializer, kernel_regularizer=regularizer)
    return normal_conv(batch_normal)


def transpose_conv(output_channels):
    initializer = tf.random_normal_initializer(0, 0.02)
    regularizer = keras.regularizers.l1(l1_weight)
    return keras.layers.Conv2DTranspose(output_channels, 3, 1, padding='same', activation='relu',
                                        kernel_initializer=initializer, kernel_regularizer=regularizer)


def conv_2(num_filter):
    initializer = tf.random_normal_initializer(0, 0.02)
    regularizer = keras.regularizers.l1(l1_weight)
    return keras.layers.Conv2D(num_filter, 2, 1, padding='same', activation='relu',
                               kernel_initializer=initializer, kernel_regularizer=regularizer)


def up_sampling2D(size):
    return keras.layers.UpSampling2D(size)


def u_net(input_shape):
    # initializer = tf.random_normal_initializer(0, 0.02)
    # [1, 512, 512, 3]
    # Encode
    input_layer1 = keras.Input(input_shape)
    block1_1 = bca(numFilter)(input_layer1)
    block1_2 = bca(numFilter)(block1_1)
    max_pooling = keras.layers.MaxPool2D(2, 2, padding='same')

    input_layer2 = max_pooling(block1_2)
    # [1, 256, 256, 64]

    block2_1 = bca(numFilter * 2)(input_layer2)
    block2_2 = bca(numFilter * 2)(block2_1)

    input_layer3 = max_pooling(block2_2)
    # [1, 128, 128, 128]

    block3_1 = bca(numFilter * 4)(input_layer3)
    block3_2 = bca(numFilter * 4)(block3_1)

    input_layer4 = max_pooling(block3_2)
    # [1, 64, 64, 256]

    block4_1 = bca(numFilter * 8)(input_layer4)
    block4_2 = bca(numFilter * 8)(block4_1)

    # drop_out = keras.layers.Dropout(rate=drop_rate)
    input_layer5 = max_pooling(block4_2)
    # [1, 32, 32, 1024]

    block5_1 = bca(numFilter * 16)(input_layer5)
    block5_2 = bca(numFilter * 16)(block5_1)

    # Decode
    # input_up_layer4 = transpose_conv(numFilter * 8)(block5_2)
    up_layer4 = conv_2(numFilter * 8)(up_sampling2D(size=(2, 2)))(block5_2)
    merge_layer4 = keras.layers.concatenate([block4_2, up_layer4])
    up_block4_1 = bca(numFilter * 8)(merge_layer4)
    up_block4_2 = bca(numFilter * 8)(up_block4_1)

    up_layer3 = conv_2(numFilter * 4)(up_sampling2D(size=(2, 2)))(up_block4_2)
    merge_layer3 = keras.layers.concatenate([block3_2, up_layer3])
    up_block3_1 = bca(numFilter * 4)(merge_layer3)
    up_block3_2 = bca(numFilter * 4)(up_block3_1)

    up_layer2 = conv_2(numFilter * 2)(up_sampling2D(size=(2, 2)))(up_block3_2)
    merge_layer2 = keras.layers.concatenate([block2_2, up_layer2])
    up_block2_1 = bca(numFilter * 2)(merge_layer2)
    up_block2_2 = bca(numFilter * 2)(up_block2_1)

    up_layer1 = conv_2(numFilter)(up_sampling2D(size=(2, 2)))(up_block2_2)
    merge_layer1 = keras.layers.concatenate([block1_2, up_layer1])
    up_block1_1 = bca(numFilter)(merge_layer1)
    up_block1_2 = bca(numFilter)(up_block1_1)

    output_layer = keras.layers.Conv2D(1, 1, activation='sigmoid')(up_block1_2)
    model = keras.Model(inputs=input_layer1, outputs=output_layer)

    return model


if '__name__' == '__main__':
    pass
