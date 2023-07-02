import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

df = pd.read_excel("weather.xlsx")
# print(df.head(5))

y = df["Basel Temperature [2 m elevation corrected]"].values.reshape(-1,1) # column vector conversion
x = df["Basel Growing Degree Days [2 m elevation corrected]"].values.reshape(-1,1)

print(x.shape)
print(y.shape)

plt.scatter(x[::1000],y[::1000])
plt.title('Basel Temp vs Basel Growing Degree Days ')
plt.xlabel("Basel Growing Degree Days")
plt.ylabel("Basel Temp")
plt.show()

x = x[~np.isnan(x).any(axis=1)]
y = y[~np.isnan(y).any(axis=1)]

print(x.shape)
print(y.shape)

xTrain , xTest , yTrain , yTest = train_test_split(x,y,test_size=0.2,random_state = 0)

lReg = LinearRegression()
lReg.fit(xTrain,yTrain)

yPrediction = lReg.predict(X=xTest)

yPrediction = pd.DataFrame ({"Actual": yTest.flatten(), "Predict":yPrediction.flatten()})
print(yPrediction.head(5))


plt.scatter(xTrain[::1000] , yTrain[::1000] , color = "red")
plt.plot(xTrain[::500] , lReg.predict(xTrain)[::500], color = "blue")
plt.title('Basel Temp vs Basel Growing Degree Days ')
plt.xlabel("Basel Growing Degree Days")
plt.ylabel("Basel Temp")
plt.show()


print("Mean Absolute Error:", mean_absolute_error(xTrain ,yTrain))
print("Mean Squared Error:",mean_squared_error(xTrain ,yTrain))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(xTrain ,yTrain)))