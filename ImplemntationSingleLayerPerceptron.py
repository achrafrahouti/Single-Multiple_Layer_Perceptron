# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 8:12:13 2021

@author: Rahouti Achraf
"""
import matplotlib.pyplot as plt

w1=0
w2=0
b=0
d1=[0,0,0,1] #pour superviser AND
d2=[0,1,1,1] #pour superviser OR
d3=[0,1,1,0] #pour superviser XOR
X=[[0,0],[0,1],[1,0],[1,1]] # les entre de neurone
alpha=0.7
E=list()


def fd(x): # la fonction  d'Activation /La fonction Heaviside
    if x<=0:
        return 0
    else:
        return 1
def fctLog(n,m): #Pour calculer la sortie de neurone
    return fd(n*w1+m*w2+b)


def apprendre(t):
    global w1,w2,b,E
    it=0
    # on va definir la valeur de d selon la fonction logique choisie par l'utilisateur
    if t==1:
        d=d1
    if t==2:
        d=d2
    if t==3:
        d=d3
    for z in range(20):
        sum=0
        for n in range(4):
            #y=fctLog(X[n][0],X[n][1])
            a=X[n][0]*w1+X[n][1]*w2 # la somme pondérée des entrées du réseau
            y=fd(a+b)                  
            e=d[n]-y
            w1=w1+alpha*e*X[n][0]     #regle de alpha
            w2=w2+alpha*e*X[n][1]     #regle de alpha
            b=b+alpha*e
            sum=sum+e*e
        E.append(sum/2)
        if sum>0:
            it+=1
    return it
def main():
    print(d1[1])
    while(1):
        E.clear()
        print("-------FONCTION LOGIQUE A APPRANDRE PAR LE PERCEPTRON MONO-COUCHE-------")
        print("ET                             1")
        print("OU                             2")
        print("XOR                            3")
        print("sortire                        0")
        print("------------------------------------------------------------------------")
        # Pour choisir La fonction a tester
        choix=int(input("choisir la fonction logique:"))
        while(choix not in range(0,4)): 
                choix=int(input("choisir la fonction logique:"))
        if choix ==1:
            print("Apprentissage de la fonction logique **ET**")
        if choix ==2:
            print("Apprentissage de la fonction logique **OU**")
        if choix ==3:
            print("Apprentissage de la fonction logique **XOR**")
        if choix ==0:
            print("\nPrograme Terminer")
            break
        it=apprendre(choix)
        print("Entrainement Terminer")
        print("**w1 =",w1)
        print("**w2 =",w2)
        print("**b  =",b)
        if it!=20:
            print("La fonction est appris dans la ",it,"iteration")
        else:
            print("La fonction pas appris")
        plt.plot(E)
        plt.title("la courbe")
        plt.show()
        res="o"
        while(res=="o"):
            print(" \n LE TEST")
            x1=int(input("Entrer x1 :"))
            x2=int(input("Entrer x2 :"))
            print("Le resultat est :====>",fctLog(x1,x2))
            res=input("tester la fonction o/n :")
            
if __name__ == "__main__":
    main()