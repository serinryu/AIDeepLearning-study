# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv('gpascore.csv')

#데이터 전처리
data = data.dropna()
y데이터 = data['admit'].values
x데이터 = []
for i, rows in data.iterrows():
  x데이터.append([rows['gre'], rows['gpa'], rows['rank']])

import numpy as np
import tensorflow as tf

#모델 만들기
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(64, activation='tanh'),
  tf.keras.layers.Dense(128, activation='tanh'),
  tf.keras.layers.Dense(1, activation='sigmoid'),
])

#model compile하기
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#model 학습(fit)시키기
model.fit(np.array(x데이터), np.array(y데이터), epochs=100) #10번

#학습시킨 model 로 예측해보기
예측값 = model.predict([ [750, 3.70, 3], [400, 2.2, 1]]) #과연??
print(예측값)
