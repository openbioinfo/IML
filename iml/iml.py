from load import load_
from desc import desc_
from select_features import select_features_
from select_models import select_models_

class iml(object):

    def __init__(self)
        self.matrix_file = None
        self.model = None
        self.args = None
        self.data = None
        self.target = None
        self.feature_names = None
        self.target_name = None
    
    def load(self,matrix_file,target_name,feature_selected=None,sep="tsv"):
        """load input file to iml-data format...

        """
        data,target,feature_names,target_name = load_(self.matrix_file)
        self.data = data
        self.target = target
        self.feature_names = feature_names
        self.target_name = target_name

    def desc(self):
        """make description for every features including, distribution and \
           statistical-anaylis 
        
        Returns: this module will output description results to `desc` directory

        """
        desc_(self.data,self.target,self.feature_names,self.target_names)


    def select_features(self):
        """select most-relavant features using RF-algorithems @sx.
        """
        selected = select_features_(self.data,self.target,self.feature_names,\
                         self.target_names)

    def use_features(self,selected):
        """
        """
        data,target,features_names,target_name = (self.data,self.target,self.features_names,self.tartets ,\
                  features_selected)
        self.data = data
        self.target = target
        

    def select_models(self):
        best_model,models  = select_models_(self.data,self.target,self.feature_names,\
                               self.target_names) 
        return best_model,models

    def load_model(self,model):
        self.model = load_model_(model,self.data,self.target,self.feature_names,\
                                 self.target_names)

    def boosting(self):
        model  = boost_(self.model,self.data,self.target,self.feature_names,\
                            self.target_names)
        self.load_model(model)

    def validate(self):
        """k-fold validation
        """
        validata_(self,model,self.data,self.target,self.feature_names,\
                            self.target_names)

    def save(self):
        """save model to file through sklean-joblib
        """
        pass

