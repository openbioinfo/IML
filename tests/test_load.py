import sys
sys.path.append("../")


from iml import iml
from iml.ext import load_tsv

mat = load_tsv()

i = iml(mat)
i.desc()
i.select_features()
i.use_features()
i.use_model()


