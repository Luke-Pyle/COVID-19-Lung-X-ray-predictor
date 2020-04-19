import cv2
import tensorflow as tf
import numpy as np
import keras
import win32com.client as wincl

CATEGORIES = ["coronavirus", "normal", "pneumonia"]

def prepare(filepath):
    IMG_SIZE = 150
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = keras.models.load_model("Lung_Detection-CNN_v7.model")

prediction = model.predict([prepare('bru.jpeg')])
roundedPrediction = np.round(prediction)

print(prediction)
y = []
for x in prediction[0]:
    y.append(int(x))

#print(CATEGORIES[y[1]])
print(y)

#print(max(roundedPrediction[0][0], roundedPrediction[0][1], roundedPrediction[0][2], roundedPrediction[0][3], roundedPrediction[0][4]))

#maxed = max(roundedPrediction[0][0], roundedPrediction[0][1], roundedPrediction[0][2], roundedPrediction[0][3], roundedPrediction[0][4])
#print(maxed)

#print(CATEGORIES[int(maxed)])
#speak = wincl.Dispatch("SAPI.SpVoice")
#speak.Speak("")



