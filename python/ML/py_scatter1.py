import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
d=pd.read_csv("iris.csv")
a=d.values
x=a[:,0:4]
y=a[:,4]

x_tr,x_te,y_tr,y_te=train_test_split(x,y,test_size=0.4,random_state=0)
'''print(x_tr,"\n",x_te,"\n",y_tr,"\n",y_te)'''
#print
#print(x,"",y)
#l=LogisticRegression(random_state=0, solver='liblinear',multi_class='multinomial').fit(x_tr,y_tr)
l=LogisticRegression(solver='liblinear')
l.fit(x_tr,y_tr)
y_pr=l.predict(x_te)
print(y_pr)
acc=accuracy_score(y_te,y_pr)
print(acc)
#print(c)'''

'''
l=LinearDiscriminantAnalysis(solver='liblinear')
l.fit(x_tr,y_tr)
'''
'''
plt.scatter(d.sepal_length,d.sepal_width)
d.plot(kind='scatter',x="sepal_length",y="sepal_width")
plt.show()
'''
'''
model_selection.KFold()
model_selection.cross_validate()
'''
