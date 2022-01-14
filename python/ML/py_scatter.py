import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
d=pd.read_csv("iris.csv")
plt.scatter(d.sepal_length,d.sepal_width)
d.plot(kind='scatter',x="sepal_length",y="sepal_width")
plt.show()
