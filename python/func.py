import pandas as pd
import numpy as np
mylist = list ("abcdefghijklmnopqrstuvwxyz")
mylist
myarr=np.arange(26)
mydict = dict(zip(mylist,myarr))
dict
ser1=pd.Series(mylist)
ser1
ser2=pd.Series(myarr)
ser2
ser3=pd.Series(mydict)
ser3.head()

