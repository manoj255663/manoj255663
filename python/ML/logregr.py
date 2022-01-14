import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report 
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
d=pd.read_csv("iris.csv")
a=d.values
x=a[:,0:4]
y=a[:,4]
x_tr,x_te,y_tr,y_te=train_test_split(x,y,test_size=0.4,random_state=0)
'''print(x_tr,"\n",x_te,"\n",y_tr,"\n",y_te)'''
l=DecisionTreeClassifier()
l.fit(x_tr,y_tr)
y_pr=l.predict(x_te)
print(y_pr)
acc=accuracy_score(y_te,y_pr)
print(acc)
#0.95
p=KNeighborsClassifier()
p.fit(x_tr,y_tr)
y_pr=p.predict(x_te)
print(y_pr)
acc1=accuracy_score(y_te,y_pr)
print(acc1)
#0.95
k=GaussianNB()
k.fit(x_tr,y_tr)
y_pr=k.predict(x_te)
print(y_pr)
acc1=accuracy_score(y_te,y_pr)
print(acc1)
#0.9333333333333
b=SVC()
b.fit(x_tr,y_tr)
y_pr=b.predict(x_te)
print(y_pr)
acc1=accuracy_score(y_te,y_pr)
print(acc1)
#0.95
class_report=classification_report(y_te,y_pr)
print(class_report)
