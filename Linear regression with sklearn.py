# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:51:40 2020

@author: Dell
"""


from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as lr 
from sklearn import metrics
import seaborn as sns

dataset=pd.read_csv("Summary of Weather.csv")
print("Whether reports during the time of WOrld War 2")
#print(dataset.info())
#print(dataset.shape)

#now plotting min temp vs max temp to get the max-min temp of a day
dataset.plot(kind="scatter",x='MinTemp',y='MaxTemp', marker='d',figsize=(10,8))
plt.title("Min-temp vs Max-temp during WW II")
plt.xlabel("Min temperature")
plt.ylabel("Max temperature")
plt.show()

#checking for the avg max temp
sns.distplot(dataset["MaxTemp"])

#as we have to find the variability in max temp according to min temp
#so storing them as follows for simplicity
x=dataset["MinTemp"].values.reshape(-1,1)
y=dataset["MaxTemp"].values.reshape(-1,1)
#reshape(-1,1) is written to represent that this data has a single feature

#now split 80% of the data to the training set while 20% of the data to test set 
#The test_size variable is where we actually specify the proportion of the test set.
x_train, x_test , y_train , y_test=tts(x,y, test_size=0.2, random_state=0, shuffle=True)
#random_state :int or RandomState instance, default=None
#Controls the shuffling applied to the data before applying the split.
#Pass an int for reproducible output across multiple function calls. 

#now training the algorithm with fit() method
regress=lr()
regress.fit(x_train,y_train) #training the algorithm

#to retrieve the intercept of the best fit line
print(regress.intercept_)

#to retrieve the slope
print(regress.coef_)

"""traing of the model done"""

"""prediction on the model begins"""

y_pred=regress.predict(x_test)

#now comparing the value of y_pred with y_test
df=pd.DataFrame({'Actual':y_test.flatten(),'Predicted':y_pred.flatten()})
print(df)
#visualising the above comparision with a bar graph
df1=df.head(20)
df1.plot(kind='bar',figsize=(8,6))
plt.show()


#plotting our data points with test data
plt.scatter(x_test,y_test,marker='d')
plt.plot(x_test,y_pred, color="deeppink",linewidth=2)
plt.plot()
#the straight line of the graph shows that our algorithm is correct

"""evaluation of the algorithm"""

#mean absolute error
print('Mean Absolute Error :',metrics.mean_absolute_error(y_test,y_pred))
#mean squared error
print('Mean Squared Error :',metrics.mean_squared_error(y_test,y_pred))
#root mean squared error
print("Root Mean Squared error:",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
#root mean squared error tells about the accuracy of the algorithm 