import np as np
import sklearn.linear_model as sk
import numpy as np
import matplotlib.pyplot as plt

y = np.array([1,1,1,1,1,2,2,2,2,2])
x = np.array([[1],[2],[3],[7],[5],[27],[28],[22],[50],[70]])
p= np.array([[-3],[40]])

model =sk.LinearRegression()
model.fit(x,y)
print(model.predict(p))