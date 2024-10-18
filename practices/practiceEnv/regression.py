import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso

bike = pd.read_csv('gongguan_best.csv')

X = bike.drop(["lent"], axis=1)
Y = bike["lent"]

lm_basic = LinearRegression()
print(cross_val_score(lm_basic, X, Y, cv=4).mean())
lm_lasso = Lasso(alpha = 0.001, max_iter=1000000)
print(cross_val_score(lm_lasso, X, Y, cv=4).mean())
lm_lasso = Lasso(alpha = 0.005, max_iter=1000000)
print(cross_val_score(lm_lasso, X, Y, cv=4).mean())
lm_lasso = Lasso(alpha = 0.01, max_iter=1000000)
print(cross_val_score(lm_lasso, X, Y, cv=4).mean())