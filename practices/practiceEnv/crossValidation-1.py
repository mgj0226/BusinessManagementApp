import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

bike = pd.read_csv('gongguan_best.csv')

X = bike.drop(["lent"], axis=1)
Y = bike["lent"]

lm = LinearRegression()
print(cross_val_score(lm, X, Y, cv=4).mean())