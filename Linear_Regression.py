# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:53:59 2020

@author: Dell
"""
from __future__ import print_function # adds compatibility to python 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#importing csv file
#CSV file (Comma Separated Values file)CSV file (Comma Separated Values file)
dataset=pd.read_csv("datasets_XY.csv")

print(dataset.head())
print(dataset.shape)
#print(dataset.describe) # describes the dimensions of the whole dataset
#print(dataset.isnull()) # to check if there is any null value in the data

#dataset.boxplot(figsize=(8,5))
print(dataset.corr())


#function to estimate the coefficients b1and b0

def cal_coeff(dataset):
    #calculating the mean of X and Y
    mean_X=np.mean(dataset.X)
    mean_Y=np.mean(dataset.Y)

    #to get total no of values in the dataset
    n=len(dataset)

    #using the formula to calculate b0 and b1
    num=0
    deno=0
    for i in range(n):
        num+=(dataset.X[i]-mean_X)*(dataset.Y[i]-mean_Y)
        deno+=(dataset.X[i]-mean_X)**2
    b1=num/deno
    b0=mean_Y-(b1*mean_X)
    return(b0,b1)

def printplot(dataset,c,m):
    plt.scatter(dataset.X,dataset.Y,color='m', marker='o',s=5)
    y_predicted=m*dataset.X+c
    plt.plot(dataset.X,y_predicted,color='green')
    plt.xlabel("Values of X")
    plt.ylabel("Values of Y")
    plt.legend()
    plt.show()
    
    
def main():
    c,m=cal_coeff(dataset)
    printplot(dataset,c,m)
    
    
if __name__=='__main__':
    main()