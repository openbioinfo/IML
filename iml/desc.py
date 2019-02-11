#!/usr/bin/env python
#-*- coding:utf8 -*-
# Powered by LongHui Deng @2019-01-24 09:00:29
from __future__ import  division,unicode_literals
from copy import copy
from io import open as open_
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False
# from scipy.stats import ttest_ind,chi2_contingency
# from load import load_,load2_,isdigit

__author__ = "Deng L.H."

###--------Tools Functions-----------------#####
def keep(x):
    return x

def isdigit(x):
    try:
        float(x)
        return True
    except:
        return False

def is_continuous (col_data):
    con = True
    if "dtype" in dir(col_data) and "%s" %(col_data.dtype) == "category":
        con = False
    return con

def fuck_encode(x):
    if isdigit(x): return str(x)
    return x

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result = dict(result, **dictionary)
    return result

def show_table(show_dict, Items = None, sep="\t"):
    resl = []
    if not Items: Items = sorted(show_dict.keys())
    for i, item in enumerate(Items):
        sub_table = show_dict[item]
        sub_items = sorted(sub_table.keys())
        if len(sub_items) == 1:
            x = "{sep_e}{mark}{item:<30}{mark}{sep}{detail}{sep_e}".format(
                mark = "" if sep != "|" else "**",
                sep_e = "" if sep != "|" else "|",
                item = item,
                sep = sep,
                detail = sep.join(map(fuck_encode, sub_table[sub_items[0]]))
            )
            resl.append(x)
            x = ""
        else:
            x = "{sep_e}{mark}{item:<30}{mark}{sep_e}".format(
                mark = "" if sep != "|" else "**",
                sep_e = "" if sep != "|" else "|",
                item = item)
            resl.append(x)
            x = ""
            for sub_item in sorted(sub_table.keys()):
                y = "{sep_e}{sub_item:>30}{sep}{detail}{sep_e}".format(
                    sep_e = "" if sep != "|" else "|",
                    item = item,
                    sep = sep,
                    sub_item = sub_item,
                    detail = sep.join(map(str, sub_table[sub_item]))
                )
                resl.append(y)
        if i == 0: 
            if sep != "|":
                x = "".join(['=']*80)
            else:
                x = "|-----|" + "|".join(["---:"] * len(sub_table[sub_items[0]]) ) + "|"
        else:
            if sep != "|":
                x = "".join(['-']*80)
        resl.append(x)
    return "\n".join(filter(lambda x: x, resl))

def load2_(infile,target_name,feature_names=None,features_maps=None,target_map=None,sep="\t"):
    """load file to IML-data object
    """
    fp = open_(infile,encoding="utf-8")
    headline = fp.readline()
    headItems = headline.strip("\n").split("\t")
    targetIdx = headItems.index(target_name)
    features = copy(headItems)
    features.pop(targetIdx)
    
    if feature_names:
        features = feature_names
        idxs = []
        for feature in feature_names:
            idx = headItems.index(feature)
            idxs.append(idx) 
    else:
        idxs = range(len(headItems))
        idxs.remove(targetIdx)
    
    data = []
    targets = []
    for line in fp.readlines():
        items = line.strip("\n").split("\t")
        datus = [ items[i] for i in idxs ]
        target = items[targetIdx]
        data.append(datus)
        targets.append(target)

    outdict = {}

    for i, feature in enumerate(features):
        col_data = map(lambda d: d[i], data)
        # del empty
        # print col_data
        subst_idx = filter(lambda i: col_data[i] , range(len(col_data)))
        col_data = map(lambda i:col_data[i], subst_idx)
        targets = map(lambda i:targets[i], subst_idx)
        
        if features_maps:
            col_data = map(features_maps[i], col_data)
        is_num = map(lambda x: isdigit(x), col_data)
        if sum(is_num)/len(col_data) < 0.9 or len(set(col_data))<= 5:
            outdict[feature] = pd.Series(col_data, dtype="category")
        else:  
            outdict[feature] = map(float, col_data)
    return pd.DataFrame(outdict), pd.DataFrame({target_name:pd.Series(targets, dtype="category")})


###-----------Basic Functions------------------#####
def Boxplot(data, targets, startmark=0):
    import matplotlib.pyplot as plt
    from pylab import mpl 
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    import seaborn as sns
    import warnings; warnings.filterwarnings(action='once')
    def add_n_obs(df,group_col,y):
        medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
        xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
        n_obs = df.groupby(group_col)[y].size().values
        for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
            plt.text(x, medians_dict[xticklabel]*1.01, "n = "+str(n_ob), horizontalalignment='center', fontdict={'size':18}, color='white')
 
    large = 22; med = 16; small = 12
    params = {'axes.titlesize': large,
            'legend.fontsize': med,
            'figure.figsize': (16, 10),
            'axes.labelsize': med,
            'axes.titlesize': med,
            'xtick.labelsize': med,
            'ytick.labelsize': med,
            'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white",{'font.sans-serif':['simhei','Arial']})


    target_name = targets.keys()[0]
    df = pd.DataFrame(dict(targets, **data))
    for i,feature_name in enumerate(data.keys()):
        plt.figure(figsize=(13,10), dpi= 80)
        sns.boxplot(x=target_name, y=feature_name, data=df, notch=False)
        add_n_obs(df,group_col=target_name,y=feature_name)   
        plt.title('Box Plot of %s' %feature_name , fontsize=22)
        plt.savefig("%02d.%s.png"%(startmark+i, feature_name))


def Pie(data, targets,startmark=0):
    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%({:d})".format(pct, absolute)

    def getAllClassLegend(df, feature_name):
        import matplotlib.pyplot as pltX
        fig, ax_tmp = pltX.subplots(subplot_kw=dict(aspect="equal"), dpi= 80)
        df = df1.groupby(feature_name).size().reset_index(name='counts')
        d = df['counts']
        categories = df[feature_name]
        wedges_AC, _, _ = ax_tmp.pie(d,
                        labels=categories,
                        autopct=lambda pct: func(pct, d),
                            textprops=dict(color="black"),
                            colors=plt.cm.Dark2.colors,
                            explode =[0]*len(categories),
                            startangle=140)
        pltX.close()
        return wedges_AC
    target_name = targets.keys()[0]
    df_all = pd.DataFrame(dict(data,**targets))
    target_vals = targets[target_name].cat.categories

    for i, feature_name in enumerate(data.keys()):
        categories = df_all[feature_name].cat.categories
        # colors = plt.cm.Dark2.colors
        # wedges_a = getAllClassLegend(df_all, feature_name)
        fig, ax = plt.subplots(nrows=1, ncols=len(target_vals), figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)
        for j, ax_s in enumerate(ax):
            df = df_all[df_all[target_name] == target_vals[j]].groupby(feature_name).size().reset_index(name='counts')
            df = df[df['counts']>0]
            d = df['counts']
            category = df[feature_name]
            idx = filter(lambda k: categories[k] in  category,  range(len(categories)))
            explode = [0.01]*len(d)
            wedges, texts, autotexts = ax_s.pie(d,
                                            labels=category,
                                            autopct=lambda pct: func(pct, d),
                                            textprops=dict(color="black"),
                                            # colors=map(lambda k:colors[k], idx),
                                            colors=plt.cm.Dark2.colors,
                                            explode = explode,
                                            startangle = 140)
            plt.setp(autotexts, size=15, weight=700)
            ax_s.set_title("%s" %(target_vals[j]))
        # ax[-1].legend(wedges_a, categories, title=feature_name, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        fig.suptitle('Pie Plot of %s' %feature_name , fontsize=22)
        plt.savefig("%02d.%s.png"%(startmark + i, feature_name))


def features_table(data, targets):
    table_out = dict()
    target_name = targets.keys()[0]
    vals = targets[target_name].cat.categories
    feature_names = sorted(data.keys())
    for i, feature_name in enumerate(feature_names):
        table_out[feature_name] = {}
        col_data = data[feature_name]
        if not is_continuous(col_data):
            for v in col_data.cat.categories:
                # table_out[feature_name][v] = map(lambda val: sum( (col_data == v) & (targets[target_name]==val)  ), vals) 
                table_out[feature_name][v] = map(lambda val: "%d(%0.2f%%)" %(
                                                  sum( (col_data == v) & (targets[target_name]==val)  ),
                                                  sum( (col_data == v) & (targets[target_name]==val)  )/sum(targets[target_name]==val)*100             ) , 
                                            vals) 
        else:
            # table_out[feature_name]["-"] = map(lambda val: "%0.2f±%0.2f" %(np.mean(col_data[targets[target_name] == val]),  
            #                                                                 np.std(col_data[targets[target_name] == val])  ) , vals) 
            table_out[feature_name]["-"] = map(lambda val: "%0.2f±%0.2f(n=%d)" %(np.mean(col_data[targets[target_name] == val]),  
                                                                            np.std(col_data[targets[target_name] == val]),  sum(targets[target_name] == val) ) , vals) 
    return table_out


def target_table(targets):
    target_name = targets.keys()[0]
    vals = targets[target_name].cat.categories
    table_out = dict()
    counts = map( lambda v:  sum(targets[target_name] == v), vals)
    table_out[target_name] = {}
    table_out[target_name]["-"] = counts
    return table_out


##-------Upper Functions--------------------###
def desc_(data_file,feature_names,target_name, target_map=keep, features_maps=[None], Osep="\t", Isep="\t"):
    show_dict = {}
    show_items = []
    
    if 1:
        _, targets = load2_(data_file, 
            target_name=target_name, 
            feature_names=[target_name],
            target_map = [target_map],
            features_maps = [target_map],
            sep = Isep
        )
        target_name = targets.keys()[0]
        vals = targets[target_name].cat.categories
        p0 = {"Items": {"-": vals} }
        p1 = target_table(targets)
        show_dict = merge_dicts(show_dict, p0, p1)
        show_items.append("Items")
        show_items.append(target_name)
    for i, feature_name in enumerate(feature_names):
        data, _ = load2_(data_file, 
            target_name=target_name, 
            feature_names=[feature_name],
            target_map = [target_map],
            features_maps = features_maps[i:i+1],
            sep = Isep
        )
        if is_continuous(data[feature_name]):
            Boxplot(data, targets, i+1)
        else:
            Pie(data, targets, i+1)
        p = features_table(data, targets)
        show_dict = merge_dicts(show_dict, p)
        show_items.append(feature_name)

    # fh = open("00.desc.txt", "w")
    fh = open_("00.desc.txt","w",encoding="utf-8")
    text = show_table(show_dict, show_items, Osep)
    fh.write(text + "\n")
    fh.close()


if __name__ == "__main__":
    def FamilyCancer(x):
        if x == "无" or not x: return "否"
        return "是"
    def Smoking(x):
        if x == "无" or not x: return "否"
        return "是"

    features_maps = [keep, keep, FamilyCancer, Smoking,
    keep, keep, keep,
    keep,
    keep, keep,
    keep, keep]

    features_selected=["性别","年龄","家族史", "吸烟史",
        "结节最大直径","Class_CtDNA","糖类抗原125 (CA125)",
        "癌胚抗原（CEA）",
        "鳞状上皮细胞癌抗原（SCC）","神经元特异性烯醇化酶（NSE）",
        "非小细胞肺癌相关抗原21-1 (CYFRA21-1)", "胃泌素释放肽前体(ProGRP) " ]
    target_name="良恶性"
 
    desc_("../tests/data/192.tsv",features_selected,target_name, target_map=keep, features_maps=features_maps, Osep="|")


