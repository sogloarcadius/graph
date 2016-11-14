#! /usr/bin/python3
#-*-coding:utf8-*-

from Graphe import *
import sys
from  math import *

############################################################
#Implementation de l'algorithme de Bellman Graphe sans circuit absorbant
#Author : SOGLO Arcadius
#Python 3.4.2
#####################################################



##############################
## Application dun nouvel algorithme qui prend en compte les circuits absorbant
#Calcul du plus court chemin
##################

def pccBellman2(graphe, s):
    """
        Parametre dentrée : objet graphe
                             le sommet s : source

        d = {}  #dictionnaire du pcc entre la source et un sommet i qui est la clé
        pred = {} #dictionnaire des predecesseurs dans ce pcc
        pas_de_circuit_absorbant=True  #indique si pas de circuit absorbant

        Contrainte : pas de circuit absorbant : circuit de longeur negative
    """
    ##Variables
    d = {} #dictionnaire du pcc entre la source et un sommet i qui est la clé
    pred = {} #dictionnaire des predecesseurs
    n=len(graphe.sommets)
    infini = float('inf') #infini en python
    pas_de_circuit_absorbant=True ## retourne vrai ssi pas de circuit absorbant
    ##initialisation
    for sommet in graphe.sommets:
        if sommet !=s:
            d[sommet]=infini
    d[s]=0

    for i in range(n):
        for (u,v) in graphe.arcs.keys():#les clés du dico sont des arcs
            #print("(u,v) : "+str((u,v)))
            #print("d[u] : "+str(d[u]))
            #print("graphe.arcs[(u,v)] : "+str(graphe.arcs[(u,v)]))
            paux = d[u] + graphe.arcs[(u,v)]
            #print("paux : " +str(paux))
            #print("d[v] : "+str(d[v]))
            if paux < d[v]:
                pred[v]=u
                d[v]=paux
            #print("pred : "+str(pred))
            #print("d : " +str(d))

    ### On refait une intération et si un chemin voir sa longeur diminué alors existence de circuit absorbant
    ###voila comment on test existence de circuit absorbant)
    for (u,v) in graphe.arcs.keys():
        if (d[u] + graphe.arcs[(u,v)]) < d[v]:
            pas_de_circuit_absorbant=False

    return d,pred,pas_de_circuit_absorbant

######################################################
#### Extraire le plus court chemin entre deux sommets
#Si chemin existe on l'extrait
#Sinon liste= [None] cost=None
####################################################

def BellmanXY2(graphe,sm1,sm2):
    """
        param In : graphe, sommet source, sommet destination

        param out : liste =[ sm1, b, sm2] : chemin entre sm1 et sm2 si existe
                    cost : int : le cout du chemin
                        --
                     liste=[None] : si pas de chemin
                     cost = None  : ||
    """
    d,pred,pas_de_circuit_absorbant =pccBellman2(graphe,sm1)
    #print(d)
    #print(pred)
    #print(pas_de_circuit_absorbant)
    if (pas_de_circuit_absorbant==True):##Contrainte algorithme Bellman
        liste=[]
        sommet=sm2
        cost=None #initiation valeur cout si pas de chemin
        if sommet in pred.keys():
            cost=d[sm2]
            liste.insert(0,sm2)
            for key,values in pred.items():
                if(pred[sommet] != sm1):
                    sget=pred[sommet]
                    liste.insert(0,sget)
                    sommet=sget
            liste.insert(0,sm1)
        else:
            liste.append(None)##si pas de chemin(pas de predecesseurs)
        #print(liste)
        #print(cost)
        return liste,cost

    else:
        sys.exit("\n"+ "@Warning"+"\n"+"Le graphe comporte au moins un circuit absorbant."+ "\n"+ "Cet algorithme ne fonctionne pas pour des graphes avec circuit absorbant." +"\n")


#####################################################
## Affiche tous les plus courts chemin
#    entre le sommet source et tous les autres sommets
##        !!! appel de BellmanXY2(voir fonction dessus)
###############

def Bellman2(graphe,s):
    """
        param In : graphe et sommet source

        Sortie : Affiche les pcc entre la source et les sommets du graphe

        !!! appel de BellmanXY2(voir fonction dessus)
    """
    chemins={} # dictionnaire des chemins
    #clé : longueur chemin
    #valeur: liste des chemins entre  S et les sommets du graphe

    print('*'*50)
    print("Recherche du plus court chemin entre {} et tous les autres sommets".format(s))
    print("*"*50)
    print('Plus courts chemin de : ')
    sommets_injoignable=[] # on stocke les sommets injoignables
    for sommet in graphe.sommets:
        if sommet !=s:
            listd,cost=BellmanXY2(graphe,s,sommet)
            if cost !=None:
                chemins[cost]=listd
                for keys,values in chemins.items():
                    print("longueur ", keys, " :", '->'.join(map(str,values)))
                chemins={}
            else :
                sommets_injoignable.append(sommet)
    #print(sommets_injoignable)
    for k in sommets_injoignable:
        print("il ny a aucun chemin de {} à {} ".format(s,k))
