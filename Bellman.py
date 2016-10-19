#-*-coding:utf8-*-

from Graphe import *

############################################################
#Implementation de l'algorithme de Bellman
#Author : SOGLO Arcadius
#Python 3.4.2
#####################################################

def choisir(graphe,sinconnu,sconnu):
    """
        input : le graphe et liste de sommet inconnu(X - E) et sommet connu(Ensemble E )
        output : un sommet ayant tous ses predecesseurs dans s_connu
    """
    sommetcandidat=[]

    for sommet in sinconnu:
        pred = graphe.predecesseurs(sommet)
        #print(str(sommet) + " : " + str(pred))
        if (all( x in sconnu for x in pred)):
            sommetcandidat.append(sommet)
    #print("sommet candidat  " + str(sommetcandidat))
    return sommetcandidat


def pccBellman( graphe, s):
    """
        Parametre dentrée : objet graphe
                             le sommet s : source
        Sortie : Affiche les plus court chemin

        Contrainte : pas de circuit absorbant : circuit a valeur negative
    """

    ##Variables
    s_connu = [] #liste de sommet dont on connait la plus courte distance(pcc)
    s_inconnu =[] #liste de sommet dont le pcc inconnu
    d = {} #dictionnaire du pcc entre la source et un sommet i qui est la clé
    pred = {} #dictionnaire des predecesseurs
    infini = 2016

    ## initialisation
    #tous les sommets sauf l'origine sont dans s_inconnu
    for vertice in graphe.sommets:
        if vertice != s:
            s_inconnu.append(vertice)

    s_connu.append(s)
    d[s]=0

    while (s_inconnu):
         sommetcandidat=choisir(graphe,s_inconnu,s_connu)
         x=min(sommetcandidat)
         #print("min :" +str(x))
         s_inconnu.remove(x)
         n=infini
         for y in graphe.predecesseurs(x):
             couple=(y,x)
             np=d[y] + graphe.arcs[couple]
             if np < n :
                 z=y
                 n=np
         d[x]=n
         s_connu.append(x)
         pred[x]=z

    return d,pred

def BellmanXY(graphe, sm1,sm2):
    d,pred =pccBellman(graphe,sm1)
    chemin={}
    liste=[]
    cost=d[sm2]
    sommet=sm2
    liste.insert(0,sm2)

    for key,values in pred.items():
        if(pred[sommet] != sm1):
            sget=pred[sommet]
            liste.insert(0,sget)
            sommet=sget
    liste.insert(0,sm1)
    return liste,cost


def Bellman(graphe,s):
    chemins={}
    for sommet in graphe.sommets:
        if sommet !=s:
            listd,cost=BellmanXY(graphe,s,sommet)
            chemins[cost]=listd
    #return chemins
    print('*'*50)
    print("Recherche du plus court chemin entre {} et tous les autres sommets".format(s))
    print("*"*50)
    print('Plus courts chemin de : ')
    for keys,values in chemins.items():
        print("longueur ", keys, " :", '->'.join(map(str,values)))
        # for val in values:
        #     print(str(val)+ "->", end=" ")


###### Application dun nouvel algorithme qui prend en compte les circuits absorbant
#Calcul du plus court chemin en utilisant l'algorithme qui tiens compte des circuitabsorbant
"""
algorithme
initialisation ( G, s)
// les poids de tous les sommets sont mis à +infini
// le poid du sommet initial à 0 ;
pour i=1 jusqu’à Nombre de sommets -1 faire
|
pour chaque arc (u, v) du graphe faire
|
| paux := poids(u) + poids(arc(u, v));
|
| si paux <poids(v) alors
|
|
| pred(v) := u ;
|
|
| poids(v) := paux;
pour chaque arc (u, v) du graphe faire
|
si poids(u) + poids(arc(u, v)) <poids(v) alors
|
retourner faux
retourner vrai

L’algorithme retourne VRAI si et seulement
si le graphe ne contient aucun circuit de longueur stric-
tement négatif accessible depuis l’origine.
"""

def pccBellman2(graphe, s):
    ##Variables
    d = {} #dictionnaire du pcc entre la source et un sommet i qui est la clé
    pred = {} #dictionnaire des predecesseurs
    n=len(graphe.sommets)
    infini = 2016
    circuitabsorbant=True ## retourne vrai ssi pas de circuit absorbant
    ##initialisation
    for sommet in graphe.sommets:
        if sommet !=s:
            d[sommet]=infini
    d[s]=0

    for i in range(n):
        for (u,v) in graphe.arcs.keys():#les clés du dico sont des arcs
            #print((u,v))
            paux=d[u] + graphe.arcs[(u,v)]
            #print(d[v])
            if paux < d[v]:
                pred[v]=u
                d[v]=paux
    for (u,v) in graphe.arcs.keys():
        if (d[u] + graphe.arcs[(u,v)]) < d[v]:
            circuitabsorbant=False
        else :
            circuitabsorbant=True
    return d,pred

def BellmanXY2(graphe, sm1,sm2):
    d,pred =pccBellman2(graphe,sm1)
    chemin={}
    liste=[]
    cost=d[sm2]
    sommet=sm2
    liste.insert(0,sm2)

    for key,values in pred.items():
        if(pred[sommet] != sm1):
            sget=pred[sommet]
            liste.insert(0,sget)
            sommet=sget
    liste.insert(0,sm1)
    return liste,cost

def Bellman2(graphe,s):
    chemins={}
    for sommet in graphe.sommets:
        if sommet !=s:
            listd,cost=BellmanXY2(graphe,s,sommet)
            chemins[cost]=listd
    #return chemins
    print('*'*50)
    print("Recherche du plus court chemin entre {} et tous les autres sommets".format(s))
    print("*"*50)
    print('Plus courts chemin de : ')
    for keys,values in chemins.items():
        print("longueur ", keys, " :", '->'.join(map(str,values)))
        # for val in values:
        #     print(str(val)+ "->", end=" ")
