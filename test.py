# 创建时间：2023/3/16 8:36
# 创建者：来自星星的奶
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
df = load_iris()
x = df['data']
y = df['target']
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=22)
translator = StandardScaler()
translator.fit(x_train)
x_train = translator.transform(x_train)
x_test = translator.transform(x_test)
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
y_predict = model.predict(x_test)