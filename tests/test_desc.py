#!/usr/bin/env python
#-*- coding:utf8 -*-
# Powered by LongHui Deng @2019-02-01 17:41:05

import sys
sys.path.append("../")
from iml.desc import desc_,keep

tsv = "data/192.tsv"

def FamilyCancer(x):
    if x == "无" or not x: return "否"
    return "是"
def Smoking(x):
    if x == "无" or not x: return "否"
    return "是"





def test_desc():
    features_maps = [keep, keep, FamilyCancer, Smoking,
                     keep, keep, keep,keep, keep, keep,keep, keep]
    features_selected=["性别","年龄","家族史", "吸烟史",
        "结节最大直径","Class_CtDNA","糖类抗原125 (CA125)",
        "癌胚抗原（CEA）",
        "鳞状上皮细胞癌抗原（SCC）","神经元特异性烯醇化酶（NSE）",
        "非小细胞肺癌相关抗原21-1 (CYFRA21-1)", "胃泌素释放肽前体(ProGRP) " ]
    target_name="良恶性"
    desc_(tsv, features_selected, target_name, target_map=keep, features_maps=features_maps, Osep="|")

if __name__ == "__main__":
    test_desc()
