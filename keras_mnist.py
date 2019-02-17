import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.datasets import mnist

numpy.random.seed(42)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_train = x_train.astype("float32")
x_train /= 255

y_train = np_utils.to_categorical(y_train, 10)

model = Sequential()
model.add(Dense(800, input_dim=784, kernel_initializer="normal", activation="relu"))
model.add(Dense(10, kernel_initializer="normal", activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
print(model.summary())

# Обучение
model.fit(x_train, y_train, batch_size=200, epochs=100, verbose=1)

# Проверка
predictions = model.predict(x_train)
predictions = np_utils.categorical_probas_to_classes(predictions)
