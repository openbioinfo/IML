#coding=utf-8

__author__ = "D J. Kong"

from copy import copy
from ext import autodetect 

def load_(infile,target_name,features_selected=None,features_maps=None,target_map=None):
    """load file to IML-data object
    """
    fp = open(infile)
    headline = fp.readline()
    headItems = headline.strip("\n").split("\t")
    targetIdx = headItems.index(target_name)
    features = copy(headItems)
    features.pop(targetIdx)
    
    if features_selected:
        features = features_selected
        idxs = []
        for feature in features_selected:
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
    for feature in features:
        outdict[feature] = []
   
    for items in data:
        for i in range(len(items)) :
            outdict[features[i]].append(items[i])

    # handle Mapping
    outmaps = {}
    outdict2 = {}
    if features_maps:
        if type(features_maps) == list:
            for i in range(len(features)):
                outmaps[features[i]] = features_maps[i]
        else:
            for i in range(len(features)):
                outmaps[features[i]] = features_maps
    else:
        for i in range(len(features)):
            outmaps[features[i]] = autodetect(outdict[features[i]])

    for feature,values in outdict.items(): 
        outdict2[feature] = [ outmaps[feature](item) for item in outdict[feature]]

    if not target_map:
        target_map = autodetect(targets)
    
    targets = [ target_map(target) for target in targets ]

    # Join Matrix
    data2 = []    
    targets2 = []

    for i in range(len(outdict2.values()[0])):
        items = []
        hasnull = False
        for feature in features:
            item  = outdict2[feature][i]
            if item == "":
                hasnull = True
            items.append(item)
        if targets[i] == "":
            hasnull = True
        
        if not hasnull:
            data2.append(items)
            targets2.append(targets[i])
    return data2,targets2,features,target_name
