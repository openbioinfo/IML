#coding=utf-8
__author__ = "D J.Kong"
from models import models
import numpy as np
from sklearn.metrics import roc_curve,auc
from sklearn.model_selection import KFold,StratifiedKFold,train_test_split
from plots import rocplots

def select_models_(data,target,features_names,target_name):
    """select models based roc metrics using k-fold cross-validation
    """
 
    X = np.array(data)
    y = np.array(target)
    kf = KFold(n_splits=10,shuffle=True,random_state=0)    
    #kf = StratifiedKFold(n_splits=5,shuffle=True,random_state=0)    
    
    metrics = []
    for name,clf in models.items():
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
        rocplots(fprs,tprs,name)
        metrics.append([name,np.mean(aucs),np.std(aucs,ddof=1)])
    
    metrics = sorted(metrics,key=lambda x:( -x[1],-x[2] ))
    best_model = models[metrics[0][0]]
    fp = open("models.metrics.tsv","w")
    head = ["name","mean_auc","std_auc"] 
    line = "\t".join(head) + "\n"
    fp.write(line)
    for metric in metrics:
        metric = [str(i) for i in metric]
        line = "\t".join(metric) + "\n"
        fp.write(line)
    fp.close()
    return best_model,models
