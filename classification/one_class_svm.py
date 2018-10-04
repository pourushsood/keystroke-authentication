# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:57:16 2018

@author: Rajdeep Biswas
"""

import numpy as np
import pandas as pd
from sklearn import svm

def svm_one_class(X_train,X_test,Y_test):
    
    # fit the model
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1) #gamma='scale' can be taken too
    clf.fit(X_train)
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)
    n_error_train = y_pred_train[y_pred_train == -1].size     #No of training mislassifiations
    positive_user = y_pred_test[y_pred_test == Y_test].size       #No of Predictions that the user is i
    negative_user = y_pred_test[y_pred_test != Y_test].size       #No of Predictions that the user is not i
    print("No of Training Misclassifications : %s" %n_error_train)
    print("Correct Decissions: %s percent" %(positive_user*100)/Y_test.size)
    print("Incorrect Decissions: %s percent" %(negative_user*100)/Y_test.size)     
    

def main():
    n = 20     #No of people
    data=[]    #Data Set
    for i in range(n):
        name= 'Hold_Times%s.csv' %i         #Assuming data files will be in same directrory and data should have integer index(0-19) in name
        df=pd.read_csv(name,header = None)
        data.append(np.array(df))
        
    data=np.array(data)
           
    for i in range(n):
        #concatinate all the list together for testing as all column size same
        if(i==0):
            test=data[1]
            for k in range (2,n):
                test=np.vstack((test,data[k]))                     #Stack the datasets together
        else:
            test=data[0]
            for k in range (1,n):
                if(k!=i):
                    test=np.vstack((test,data[k]))                 #Stack the datasets together 
                
            
        print("For User %s" %i)
        print()
        for j in range (5):                                       #5 Fold cross validation
            print("Iteration %s:" %j)
            data_train=data[i]
            np.random.shuffle(data_train)            
            sz=int(0.05*data_train.shape[0])+1
            data_train_final=data_train[:-sz]                     #Discarding last 5% entries for training and add them in tesing
            data_test_final=data_train[-sz:] 
            y=np.ones(sz)
            
            sz=int(0.25*data_train_final.shape[0])-sz+1            #No of test sample needed more for 80:20 ratio
            np.random.shuffle(test)                               #Shuffle the whole set for testing
            data_test_final=np.vstack((data_test_final,test[:sz]))
            z=-np.ones(sz)
            y_final=np.append((y,z),axis=0)                       #Result vector for Testing
            svm_one_class(data_train_final,data_test_final,y_final)       # calling SVM function
              
    
    
main()
