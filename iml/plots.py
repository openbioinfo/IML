#coding=utf-8
import random 
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def rocplot(fpr,tpr,name):
    
    plt.figure()
    plt.plot(fpr,tpr,color="black",lw=2)
    plt.plot([0,1],[0,1],color="gray",linestyle="--",lw=2)
   
    plt.xlim(-0.05,1) 
    plt.ylim(0,1.1)

    plt.xlabel("1-specifity")
    plt.ylabel("sensitivity")

    png = name + ".roc.png"
    plt.savefig(png)
    plt.close()

def rocplots(fprs,tprs,name):

    plt.figure()
    for fpr,tpr in zip(fprs,tprs):
        plt.plot(fpr,tpr,lw=1)
    plt.plot([0,1],[0,1],color="gray",linestyle="--",lw=2)

    plt.title(name)
    plt.xlim(-0.05,1)
    plt.ylim(0,1.1)

    plt.xlabel("1-specifity")
    plt.ylabel("sensitivity")

    png = name + ".rocs.png"
    plt.savefig(png)
    plt.close()


def score_scatter(x,y,name):
    ss = {}
    for score,stage in zip(x,y):

        if stage in ss:
            ss[stage].append(score)
        else:
            ss[stage] = [score]

    data = []
    for k in sorted(ss.keys()):
        vs = ss[k]
        data.append(vs)
        m = np.mean(vs)
        std = np.std(vs,ddof = 1)
   
        items = [k,m,std] 
        items = [str(it) for it in items]

    plt.violinplot(data,widths=0.5,showextrema=False)

    xx = []
    yy = []

    for k in sorted(ss.keys()):
    
        vs = ss[k]
        k = int(k)

        for v in vs:
            f = random.choice([1,-1])
            x = k + 1 +  f * float(random.randint(0,10))/100
            xx.append(x)
            yy.append(v)

    plt.scatter(xx,yy,s=10,c="gray")
    plt.xticks([1,2],["class1","class2"])
    out = name + ".png"
    plt.savefig(out)
    plt.close()


def learnplot(x,train_error,test_error):
    
    plt.figure()
    plt.plot(x,train_error,'o-',color = 'r',label = 'training')
    plt.plot(x,test_error,'o-',color='g',label="validation")
    plt.legend(loc="best")
    plt.title("learning curve")
    plt.xlabel("sample size")
    plt.ylabel("error rate")
    plt.ylim(0,0.5)
    plt.savefig("learing-curve.png")
    plt.close()

