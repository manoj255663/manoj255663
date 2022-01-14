import pandas as pd
import numpy as np
mylist = list('abcdefghijklmnopqrstuvwxyz')
print(mylist)
myarr = np.arange(26)
mydict = dict(zip(mylist,myarr))
print(dict)
ser1=pd.Series(mylist)
print(ser1)
ser2=pd.Series(myarr)
print(arr)
ser3=pd.Series(mydict)
print(ser3.head())
