

def percent(i,default=''):
    try:
        i = i[:-1]
        return float(i)/100
    except:
        return default
    

def typeofit(i):

    if type(i) == int:
        return Int
    if type(i) == float:
        return Float
    
    if i.isdigit():
        return Int
    try:
        float(i)
        return Float
    except:
        if i.endswith("%"):
            return percent
        else:
            return str
    
def autodetect(items):
    
    types = [ typeofit(it) for it in items if it ]
    types = list(set(types))

    if len(types) == 1 and types[0] != str:
        return types[0]
    else:
        cls = list(set(items))
        return genMap(cls)

def Int(i,default=''):
    
    try:
        j = int(i)
    except:
        j = default
    return j

def Float(i,default=''):
    
    try:
        j = float(i)
    except:
        j = default


def genMap(cls):
    tempdict = {}
    for i in range(len(cls)):
        tempdict[cls[i]] = i
    def map(acls):
        return tempdict[acls]
    return map

#amap =  genMap(["A","B","C"])
#print amap("A")
#amap =  genMap(["B","C","F"])
#print amap("F")
#print autodetect([1,2,3])("1.2")
