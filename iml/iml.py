from load import load_
from desc import desc_
from select_features import select_features_
from select_models import select_models_

class iml(object):

    def __init__(self,matrix_file)
        self.matrix_file = matrix_file
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
        """select most-relavant features using RF-algorithems.
        """
        selected = select_features_(self.data,self.target,self.feature_names,\
                         self.target_names)

    def use_features(self,selected):
        self.load(self.data,self.target,self.features_names,self.tartets ,\
                  features_selected)

    def select_models(self):
        model = select_models_(self.data,self.target,self.feature_names,\
                               self.target_names) 

    def use_model(self,model):
        self.model = model

    def boosting(self):
        args,model = boost_(self.model,self.data,self.target,self.feature_names,\
                            self.target_names)
        self.args = args
        self.model = model

    def validate(self):
        """k-fold validation
        """
        validata_(self,model,self.data,self.target,self.feature_names,\
                            self.target_names)

    def save(self):
        """save model to file through sklean-joblib
        """
        pass

