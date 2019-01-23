#coding=utf-8
import sys
sys.path.append("../")

from iml.load import load_

tsv = "data/192.tsv"
def test_load():
    load_(tsv,target_name="良恶性",features_selected=["年龄","性别"])

if __name__ == "__main__":
    test_load()
