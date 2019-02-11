from load import load_
from desc import desc_
from select_features import select_features_
from use_features import use_features_
from select_models import select_models_
from load_model import load_model_
from boosting import boosting_
from validate import validate_
from sklearn.externals import joblib

class iml(object):

    def __init__(self):
        self.matrix_file = None
        self.model = None
        self.args = None
        self.data = None
        self.target = None
        self.feature_names = None
        self.target_name = None
    
    def load(self,matrix_file,target_name,feature_names=None,features_maps=None,target_map=None):
        """load input file to iml-data format...

        """
        data,target,feature_names,target_name = load_(matrix_file,target_name,feature_names,features_maps,target_map)
        self.data = data
        self.target = target
        self.feature_names = feature_names
        self.target_name = target_name


    def select_features(self):
        """select most-relavant features using RF-algorithems @sx.
        """
        selected = select_features_(self.data,self.target,self.feature_names,\
                         self.target_name)
        return selected

    def use_features(self,selected):
        """
        """
        data,target,feature_names,target_name = use_features_(self.data,self.target,self.feature_names,self.target_name ,selected)
        self.data = data
        self.feature_names = feature_names
        
    def select_models(self):
        best_model,models  = select_models_(self.data,self.target,self.feature_names,\
                               self.target_name) 
        return best_model,models

    def use_model(self,model):
        self.model = load_model_(model,self.data,self.target,self.feature_names,\
                                 self.target_name)

    def boosting(self):
        model  = boosting_(self.model,self.data,self.target,self.feature_names,\
                            self.target_name)
        self.use_model(model)

    def validate(self):
        """k-fold validation
        """
        validate_(self.model,self.data,self.target,self.feature_names,\
                            self.target_name)

    def save(self):
        """save model to file through sklean-joblib
        """
        joblib.dump(self.model,"model.m")

