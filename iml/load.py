
def load_(infile,target_name,features_selected,sep="\t"):

    fp = open(infile)
    headline = fp.readline()
    headItems = headline.strip("\n").split("\t")
    targetIdx = headitems.index(target_name)
    features = headItems.pop(targetIdx)
    if features_selectetd:
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

    return data,targets,features,target_name
