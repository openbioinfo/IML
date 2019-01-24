#coding=utf-8
__author__ = "D J.Kong"
from models import models
import numpy as np
from sklearn.metrics import roc_curve,auc
from sklearn.model_selection import KFold,StratifiedKFold,train_test_split
from plots import rocplots,learnplot
from sklearn.model_selection import learning_curve

def validate_(model,data,target,features_names,target_name):
    """select models based roc metrics using k-fold cross-validation
    """
    clf = model 
    X = np.array(data)
    y = np.array(target)
    kf = KFold(n_splits=10,shuffle=True,random_state=0)    
    #kf = StratifiedKFold(n_splits=5,shuffle=True,random_state=0)    
    aucs = [] 
    fprs = []
    tprs = []
    for train_index,test_index in kf.split(X,y):
        X_train,X_test = X[train_index],X[test_index]
        y_train,y_test = y[train_index],y[test_index]
        clf.fit(X_train,y_train)
        probas = clf.predict_proba(X_test)
        fpr,tpr,thresholds = roc_curve(y_test,probas[:,1])
        clf_auc = auc(fpr,tpr)  
        aucs.append(clf_auc)
        fprs.append(fpr)
        tprs.append(tpr)
    
    rocplots(fprs,tprs,"cross-validation")
    fp = open("cross-validation.tsv","w")
    line = "mean-auc: %s\n" % np.mean(aucs)
    fp.write(line)
    line = "std-auc: %s\n" % np.std(aucs,ddof=1)
    fp.write(line)

    train_sizes,train_score,test_score = learning_curve(clf,X,y,train_sizes=[0.1,0.2,0.4,0.6,0.8,1],\
                                                        cv=10,shuffle=True,random_state=0,scoring='accuracy')
    train_error =  1- np.mean(train_score,axis=1)
    test_error = 1- np.mean(test_score,axis=1)
    
    learnplot(train_sizes,train_error,test_error) 



