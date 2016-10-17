#-*-coding:utf8-*-

from Graphe import *

############################################################
#Implementation de l'algorithme de Bellman
#Author : SOGLO Arcadius
#Python 3.4.2
#####################################################

def choisir(graphe,sinconnu,sconnu):
    """
        input : le graphe et liste de sommet
        output : un sommet ayant tous ses predecesseurs dans s_connu
    """
    sommetcandidat=[]

    for sommet in sinconnu:
        pred = graphe.predecesseurs(sommet)
        #print(str(sommet) + " : " + str(pred))
        if (all( x in sconnu for x in pred)):
            sommetcandidat.append(sommet)
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
