#let's write a library
import random
from graphics import *

def zeros(n):
    a=[]
    for i in range(n):
        a=a+[0]
    return a

def sum_array(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]
    return s

def avg(a):
    return sum_array(a)

def var(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]**2
    m=avg(a)
    return (s/len(a)-m**z)

def rand_array(n,mini,maxi):
    a=[]
    for i in range(n):
        a=a+[random.uniform(mini,maxi)]
    return a

def histogram(mini,maxi,bins,a):
    h=zeros(bins)
    w=(maxi-mini)/bins
    for i in range(len(a)):
        for j in range(bins):
            if (a[i]>(mini+j*w) and a[i]<(mini+(j+1)*w)):
                h[j]=h[j]+1
    return h

def maximum(a):
    m=0
    for i in range(len(a)):
        if a[i]>m:
            m=a[i]
    return m

def bargraph(a):
    win=GraphWin()
    win.setCorrds(-1,-1,len(a)+1,maximum(a)+1)
    bl=[]
    tr=[]
    rec=[]
    for i in range(len(a)):
        bl=bl+[Point(i,0)]
        tr=tr+Point(i+1,a[i])
        rec=rec+[Rectangle(bl[i],tr[i])]
        rec[i].draw(win)



def main():
    a=zeros(40)
    for i in range(len(a)):
        a[i]=sum_array(rand_array(10,0,1))
    histo=histogram(0,19,7,a)
    bar_graph(histo)
main()
