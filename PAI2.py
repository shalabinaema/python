import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
x=np.array([[1],[2],[7],[5],[8],[9],[10],[2],[6]])
y=np.array([[2],[5],[7],[12],[15],[15],[20],[25],[27]])
p=np.array([[15],[25],[26]])

print(x.shape)
print(y.shape)

manger = LinearRegression()
manger.fit(x,y)
print(manger.predict(p))