from models import modelsParams
from sklearn.model_selection import GridSearchCV

def boosting_(model,data,target,features_names,target_name):

    model_name = model.__repr__().split("(")[0]
    grid_search = GridSearchCV(model,modelsParams[model_name],cv=5)
    grid_search.fit(data,target)
    
    return grid_search.best_estimator_

