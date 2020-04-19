import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import time
from keras.utils import to_categorical

NAME = "Lung-Covid_19-Detection-cnn-64x2-{}".format(int(time.time()))

X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))

X = X/150
y = to_categorical(y)

#Build the neural network
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (3, 3), input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation("relu"))


model.add(Dense(3))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

#model.summary()
model.fit(X, y, batch_size=64, epochs=20, validation_split=0.2)

model.save('Lung_Detection-CNN_v9.model')
print("Model Saved!")
