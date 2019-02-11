
def use_features_(data,target,features_names,target_name,selected):
    
    """
        only load selected features...

    """

    sidxs = [ features_names.index(sel) for sel in selected ]

    data2 = []

    for record in data:
        items = [ record[idx] for idx in sidxs ]
        data2.append(items)

    return data2,target,selected,target_name
