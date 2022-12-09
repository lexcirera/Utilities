#Question 1
import numpy as np
def conversion_fichier_mesure(fichier):
    mesure=open(fichier,'r')
    L=mesure.readlines()
    mesure.close()
    nm=len(L)//2
    vt=[None]*(nm-1)
    va=[None]*(nm-1)
    k=0
    offset=332.4
    gain=2*9.81/140
    for i in range (2,len(L),2):
        vt[k]=float(L[i].rstrip('\n').split(',')[0])
        va[k]=(int(L[i].rstrip('\n').split(',')[1])-offset)*gain
        k+=1
    return nm,vt,va
nm, temps, acc=conversion_fichier_mesure('test10.txt')

#Question 2
import matplotlib.pyplot as pl
def courbe_acc_temps(fichier):
    a,abs,ord=conversion_fichier_mesure(fichier)
    pl.clf()
    pl.plot(abs,ord,"rx")
    pl.legend('Acc',loc='lower right')
    pl.grid()
    pl.xlabel('temps')
    pl.ylabel('Accélération')
    pl.title('Courbe représentant l’accélération en fonction du temps')
    pl.show()
#Question 2bis
pl.figure(1)
pl.plot(temps,acc,'r')
pl.show()

#Question 3
def integrationG(x,y):
    n=len(y)
    v=np.zeros(n)
    v[0]=y[0]*(x[1]-x[0])
    for i in range (n-1):
        s=y[i]*(x[i+1]-x[i])
        v[i]=v[i-1]+s
    v[-1]=v[-2]+y[-1]*(x[-1]-x[-2])
    return v

vitesse=integrationG(temps,acc)
pl.figure(2)
pl.plot(temps,vitesse)
pl.show