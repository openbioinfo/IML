#coding=utf-8
import sys
sys.path.append("../")
from iml.select_models import select_models_
from iml.boosting import boosting_
from iml.load import load_
from iml.validate import validate_
tsv = "data/192.tsv"

def test_load():
    data,target,features,name = load_(tsv,target_name="良恶性",features_selected=["年龄","性别"])
    best,models = select_models_(data,target,features,name)
    model = boosting_(best,data,target,features,name)
    validate_(model,data,target,features,name)

if __name__ == "__main__":
    test_load()

