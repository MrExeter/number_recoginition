import os
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

    # Load model data to evaluate
    model = tf.keras.models.load_model('models/mnist_handwritten_numbers.keras')

    # Evaluate model
    loss, accuracy = model.evaluate(xtest, y_test)

    print("Loss: ", loss)
    print("Accuracy: ", accuracy)

