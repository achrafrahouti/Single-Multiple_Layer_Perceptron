# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 10:12:13 2021

@author: Rahouti Achraf
"""
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
cl=MLPClassifier(activation='relu',max_iter=1000,alpha=0.0001)
d1=[0,0,0,1] #pour superviser AND
d2=[0,1,1,1] #pour superviser OR
d3=[0,1,1,0] #pour superviser XOR
X=[[0,0],[0,1],[1,0],[1,1]] # les entrer de neurone
def apprendre(t):
    # on va definir la valeur de d selon la fonction logique choisie par l'utilisateur
    if t==1:
        d=d1
    if t==2:
        d=d2
    if t==3:
        d=d3
    cl.fit(X,d)
    plt.plot(cl.loss_curve_)
    plt.title("la courbe")
    plt.show()
def main():
    while(1):
        print("-------FONCTION LOGIQUE A APPRANDRE PAR LE PERCEPTRON MULTI-COUCHE-------")
        print("ET                             1")
        print("OU                             2")
        print("XOR                            3")
        print("sortire                        0")
        print("------------------------------------------------------------------------")
        
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
        apprendre(choix)
        print("Entrainement Terminer")

        res="o"
        while(res=="o"):
            print(" \n LE TEST")
            x1=int(input("Entrer x1 :"))
            x2=int(input("Entrer x2 :"))
            print("Le resultat est :====>",cl.predict([[x1,x2]]))
            res=input("tester la fonction o/n :")
            
if __name__ == "__main__":
    main()
