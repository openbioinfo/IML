#coding=utf-8
import sys
sys.path.append("../")
from iml.iml import iml


def test_iml():
    i = iml()
    i.load("data/192.tsv",target_name="良恶性",feature_selected=["年龄","性别"])
    fs = i.select_features()
    i.use_features(fs)
    best_model,models = i.select_models()
    i.use_model(best_model)
    i.boosting()
    i.validate()
    i.save()

if __name__ == "__main__":
    test_iml()



