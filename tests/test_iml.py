import sys
sys.path.append("../")


from iml import iml

i = iml()
i.load("xx.tsv")
i.desc()
i.select_features()
i.use_features()
i.use_model()


