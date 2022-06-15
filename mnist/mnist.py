from __future__ import absolute_import, division, print_function, \
  unicode_literals

import tensorflow as tf


def train_model():
  mnist = tf.keras.datasets.mnist
  # 下载 mnist 数据集，可以离线提前下载后填写路径
  # 不填就要走公网下载数据了，数据量不大，十多兆
  (x_train, y_train), (x_test, y_test) = mnist.load_data()
  x_train, x_test = x_train / 255.0, x_test / 255.0

  model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
  ])

  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
  model.fit(x_train, y_train, epochs=5)
  model.evaluate(x_test, y_test)


if __name__ == '__main__':
  train_model()
