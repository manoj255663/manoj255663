import keras
import pandas as pd
from sklearn.model_selection import train_test_split

#Required Data
data=pd.read_csv("Data_Training.csv")
data.dropna(inplace=True)
data_2019=pd.read_csv("Data_Testing_2019.csv")
#data_2019.drop(columns=["Unnamed:0"],inplace=True)

x=data.drop(columns=["Output"])
x=data.drop(columns=["Output","match_url"])
y=data.Output
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=64)
x_2019=data_2019.drop(columns=["Match","Team1","Team2"])

#converting categorical data to categorical
num_categories=2
y_train=keras.utils.to_categorical(y_train,num_categories)
y_test=keras.utils.to_categorical(y_test,num_categories)

#MOdel Building
model=keras.models.Sequential()
model.add(keras.layers.Dense(50,activation="relu",input_dim=42))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(80,activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(100,activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(2,activation="softmax"))

#Compiling the model-adadelta - Adaptive learning

model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

#Training and evaluating
batch_size=50
num_epoch=1000
model_log=model.fit(x_train,y_train,batch_size=batch_size,epochs=num_epoch,verbose=1,validation_data=[x_test,y_test])
#epoch=no.of iteration
train_score=model.evaluate(x_train,y_train,verbose=0)
test_score=model.evaluate(x_test,y_test,verbose=0)
print('Train accuracy:',train_score[1])
print('Test accuracy:',train_score[1])

#Predictions for the 2019 World Cup
prediction_2019=model.predict_classes(x_2019)
data_2019["Result"]=prediction_2019

def winner(x):
    if x.Result==1:
        x["Winning_Team"]=x.Team1
    else:
        x["Winning_Team"]=x.Team2
    return x

data_2019_final=data_2019.apply(winner,axis=1)
results_2019=data_2019_final.groupby("Winning_Team").size()
result_2019=results_2019.sort_values(ascending=False)
print(results_2019)
