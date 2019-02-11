#coding=utf-8
import sys
sys.path.append("../")
from iml.select_features import select_features_
from iml.load import load_

tsv = "data/192.tsv"

def test_load():
    data,target,features,name = load_(tsv,target_name="良恶性",features_selected=["年龄","性别"])

    s = select_features_(data,target,features,name)
    print s

if __name__ == "__main__":
    test_load()

