#coding=utf-8

__author__ = "D J. Kong"

import numpy as np
from sklearn.ensemble import RandomForestClassifier

def select_features_(data,target,features_names,target_name,tops=10):

    """
        select features using randomforeset algorithem...

    """    

    X = np.array(data)
    y = np.array(target)

    rfc = RandomForestClassifier(random_state=0)
    rfc.fit(X,y)
    imps = rfc.feature_importances_
    names = features_names
    fs = zip(imps,names)
    fs = sorted(fs,key=lambda x: -x[0])

    features_sorted = [ f[1] for f in fs ]

    return features_sorted[:tops]
