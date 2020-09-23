from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np

class Othello():
    def __init__(self, inputs, outputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.inputs = inputs
        self.outputs = outputs
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(inputs, )))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dense(outputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def train(self, dataset):
            inputs = []
            output = []
            for data in dataset:
                input.append(data[1])
                output.append(data[0])

            X = np.array(inputs).reshape((-1, self.inputs))
            y = to_categorical(output, num_classes=3)
            # Train and test data split
            boundary = int(0.8 * len(X))
            X_train = X[:boundary]
            X_test = X[boundary:]
            y_train = y[:boundary]
            y_test = y[boundary:]
            self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
            return self.model.predict(np.array(data).reshape(-1, self.inputs))[0][index]