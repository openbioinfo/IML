from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression,LogisticRegressionCV
from sklearn import neighbors 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
import inspect ,re
 
rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()
lrc = LogisticRegression()
knc = neighbors.KNeighborsClassifier()
ldc = LinearDiscriminantAnalysis()
svc = svm.SVC(probability=True)
nbc = MultinomialNB(alpha = 0.01)
dtc = tree.DecisionTreeClassifier()


clfs = [rfc,gbc,lrc,knc,ldc,svc,nbc,dtc]

models = {}
modelsParams = {}

for clf in clfs :
    name = clf.__repr__().split("(")[0]
    models[name] = clf

RandomForestClassifier_params = {
    'n_estimators'      : range(5,100,10),
    'criterion'         :["gini","entropy"],
    'min_samples_leaf'  :[2,4,6,8,10]
}

GradientBoostingClassifier_params = {
    'n_estimators'      : range(5,100,10),

}



LogisticRegression_params = {
    'penalty':["l1","l2"],
}


KNeighborsClassifier_params = {
    'n_neighbors'   : range(1,20),
    'leaf_range'    : range(1,2),
    'weight_options': ["uniform","distance"],
    "algorithm_options": ['auto','ball_tree','kd_tree','brute']
}

LinearDiscriminantAnalysis_params = {
    'solver':("eigen",),
    "shrinkage":('auto',)
}



SVC_params = [
    {
        'kernel':('rbf'),
        'gamma': [1e-3, 1e-4], 
        'C':[1, 10,100,1000]
    },
    {
        "kernel": ("linear"),
        "C":[1,10,100,1000]

    }
]

MultinomialNB_params = {}
DecisionTreeClassifier_params = {}

for name,clfs in models.items():
    modelsParams[name] = eval(name+"_params")

