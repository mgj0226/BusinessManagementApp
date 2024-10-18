import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

bike = pd.read_csv('gongguan_best.csv')

x = bike.drop(["lent"], axis=1)
y = bike["lent"]

train_X, valid_X, train_Y, valid_Y = train_test_split(x, y, test_size=0.3, random_state=0)

lm = LinearRegression()
lm.fit(train_X, train_Y)
print("R Square: ", lm.score(train_X, train_Y))

predicted_Y = lm.predict(valid_X)
rss = ((predicted_Y - valid_Y) ** 2).mean()
tss = ((valid_Y.mean() - valid_Y) ** 2).mean()
print(1 - rss / tss)