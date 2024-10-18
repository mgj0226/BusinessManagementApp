import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

bike = pd.read_csv('gongguan.csv')
print(bike.head())

lm = LinearRegression()

lent = bike["lent"].values.reshape(-1, 1)
pre = bike["precipitation"].values.reshape(-1, 1)

# lm.fit(pre, lent)

# print("Coefficient: ", lm.coef_)
# print("Intercept: ", lm.intercept_)
# print("R Square: ", lm.score(pre, lent))

temp = bike["temperature"].values.reshape(-1, 1)
tempSq = pow(temp, 2)
X_temp = np.hstack((temp, tempSq))

# lm.fit(temp, lent)

# print("Coefficient: ", lm.coef_)
# print("Intercept: ", lm.intercept_)
# print("R Square: ", lm.score(X_temp, lent))

working = bike["workingday"].values.reshape(-1, 1)
hourFactor = pd.get_dummies(bike["hour"])

X_full = np.hstack((hourFactor, working, temp, tempSq, pre))

lm.fit(X_full, lent)

# print("Coefficient: ", lm.coef_)
# print("Intercept: ", lm.intercept_)
# print("R Square: ", lm.score(X_full, lent))

bike_future = pd.read_csv('gongguan_future.csv')
print(bike_future.head())

hourFactor = pd.get_dummies(bike_future["hour"])
working = bike_future["workingday"].values.reshape(-1, 1)
temp = bike_future["temperature"].values.reshape(-1, 1)
tempSq = pow(temp, 2)
pre = bike_future["precipitation"].values.reshape(-1, 1)

X_future = np.hstack((hourFactor, working, temp, tempSq, pre))

lent_predict = lm.predict(X_future)

print(lent_predict)