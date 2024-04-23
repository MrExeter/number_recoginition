import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


if __name__ == '__main__':
    # Load MNIST handwritten number dataset
    mnist = tf.keras.datasets.mnist

    # Load training and test data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalize training and test data
    xtrain = tf.keras.utils.normalize(x_train, axis=1)
    xtest = tf.keras.utils.normalize(x_test, axis=1)

    # Define Model, flatten image from 2d 28 X 28 pixels to a flat line of 784 elements
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    # Compile model
    model.compile( optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])

    # Fit the model
    model.fit(xtrain, y_train, epochs=5)

    # Save Model to directory and filename of choice
    model.save('models/mnist_handwritten_numbers.keras')

    print("Bingo!  Done")








