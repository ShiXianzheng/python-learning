import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pathlib
# import pandas as pd
from tensorflow.python.data.ops.dataset_ops import AUTOTUNE

print(tf.version)
np.set_printoptions(precision=4)

label_path = 'E:/2019Xzshi/tf_beta2/raw_building_datasets/label_logical_datasets'
image_path = 'E:/2019Xzshi/tf_beta2/raw_building_datasets/optical_image_datasets'
label_root = pathlib.Path(label_path)
image_root = pathlib.Path(image_path)

all_images_path = list(image_root.glob('*.png'))
all_images_path = [str(path) for path in all_images_path]
image_count = len(all_images_path)
all_labels_path = list(label_root.glob('*.png'))
all_labels_path = [str(path) for path in all_labels_path]
# list string

path_imgds = tf.data.Dataset.from_tensor_slices(all_images_path)
path_labds = tf.data.Dataset.from_tensor_slices(all_labels_path)

t_img = plt.imread(all_images_path[55])
t_lab = plt.imread(all_labels_path[55])
t_lab = t_lab  # * 255.0
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(t_img)
plt.subplot(1, 2, 2)
plt.imshow(t_lab)

# <TensorSliceDataset shapes: (), types: tf.string>


def load_and_preprocess_image(path):
    image1 = tf.io.read_file(path)
    image1 = tf.io.decode_image(image1, channels=3, dtype=tf.dtypes.float32)
    image1 = tf.image.resize(image1, (512, 512))
    # return image1
    return image1 / 255.0


def load_label(path):
    label1 = tf.io.read_file(path)
    label1 = tf.io.decode_image(label1, channels=1, dtype=tf.dtypes.float32)
    label1 = tf.image.resize(label1, (512, 512))
    return label1


# img = load_and_preprocess_image(all_images_path[10])
image_ds = path_imgds.map(load_and_preprocess_image)
label_ds = path_labds.map(load_label)

for n, image in enumerate(image_ds.take(2)):
    plt.subplot(1, 2, n + 1)
    plt.imshow(image)

for n, label in enumerate(label_ds.take(2)):
    plt.subplot(1, 2, n+1)
    plt.imshow(label)

image_label_ds = tf.data.Dataset.zip((image_ds, label_ds))
# <ZipDataset shapes: (<unknown>, <unknown>), types: (tf.float32, tf.float32)>


# train
# 被充分打乱
# 被分割为batch
# 永远重复
# 尽快提供batch
BATCH_SIZE = 2
ds = image_label_ds.shuffle(buffer_size=image_count)
ds = ds.repeat()
ds.ds.batch(BATCH_SIZE)
ds = ds.prefetch(buffer_size=AUTOTUNE)

ds1 = image_label_ds.apply(
  tf.data.experimental.shuffle_and_repeat(buffer_size=image_count))
ds1 = ds1.batch(BATCH_SIZE)
ds1 = ds1.prefetch(buffer_size=AUTOTUNE)


if '__name__' == '__main':
    pass



