import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

from tensorflow.keras.datasets import mnist

from tensorflow.keras.utils import to_categorical

from mnist.repository.mnist_repository import MnistRepository


class MnistRepositoryImpl(MnistRepository):

    def loadData(self):
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        return X_train, y_train, X_test, y_test

    def preprocessData(self, X_train, y_train, X_test, y_test):
        X_train, X_test = X_train / 255.0, X_test / 255.0
        y_train, y_test = to_categorical(y_train, num_classes=10), to_categorical(y_test, num_classes=10)
        return X_train, y_train, X_test, y_test

    def buildModel(self):
        model = Sequential([
            Flatten(input_shape=(28, 28)),
            Dense(128, activation='relu'),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax'),
        ])
        return model

    def compileModel(self, buildModel):
        buildModel.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    def trainModel(self, buildModel, X_train, y_train):
        buildModel.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    def evaluateModel(self, buildModel, X_test, y_test):
        _, accuracy = buildModel.evaluate(X_test, y_test)
        return accuracy
