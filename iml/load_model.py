#coding=utf-8
__author__ = "D J.Kong"
import numpy as np
from sklearn.metrics import roc_curve,auc
from plots import rocplot
from plots import score_scatter

def load_model_(model,data,target,features_names,target_name):
    
    X = np.array(data)
    y = np.array(target)
    model.fit(data,target)

    probas = model.predict_proba(X)
    fpr,tpr,thresholds = roc_curve(y,probas[:,1])
    
    rocplot(fpr,tpr,"training_on_all")
    score_scatter(probas[:,1],y,"training_scatter")

    return model


