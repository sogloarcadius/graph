#! /usr/bin/python3
#-*-coding:utf8-*-

from Graphe import *
import sys
from  math import *

############################################################
#Implementation de l'algorithme de Bellman graphe sans circuit
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


#######
#fonction qui Calcul l'infini
###somme de tous les |poids| du graphe multiplié par 2


####
#Calcul des plus court chemin : applique algo vu en cours
###
def pccBellman(graphe, s):
    """
        Parametre dentrée : objet graphe
                             le sommet s : source
        Sortie :
            d = {} : dictionnaire du pcc entre la source et un sommet i qui est la clé
            pred = {} #dictionnaire des predecesseurs dans ce pcc

        Contrainte : pas de circuit
    """

    ##Variables
    s_connu = [] #liste de sommet dont on connait la plus courte distance(pcc)
    s_inconnu =[] #liste de sommet dont le pcc inconnu
    d = {} #dictionnaire du pcc entre la source et un sommet i qui est la clé
    pred = {} #dictionnaire des predecesseurs

    infini = float('inf')#infini en python
    #print(infini)

    ## initialisation
    #tous les sommets sauf l'origine sont dans s_inconnu

    for vertice in graphe.sommets:
        if vertice != s:
            s_inconnu.append(vertice)

    s_connu.append(s)
    d[s]=0
    try :
        while (s_inconnu):
            sommetcandidat=choisir(graphe,s_inconnu,s_connu)
            x=min(sommetcandidat)
            #print("min :" +str(x))
            #print("s_inconnu"+str(s_inconnu))
            s_inconnu.remove(x)
            #print("s_inconnu"+str(s_inconnu))
            n=infini
            for y in graphe.predecesseurs(x):
                couple=(y,x)
                #print("couple(y,x)" +str(couple))
                np=d[y] + graphe.arcs[couple]
                #print("var np :" + str(np))
                if np < n :
                    z=y
                    n=np
            d[x]=n
            #print("var z :" + str(z))
            s_connu.append(x)
            pred[x]=z
        return d,pred
    except:
        sys.exit("\n"+ "@Warning"+"\n"+
        "#cas 1 \n"+
        "Le graphe comporte au moins un circuit."+
        "\n"+ "Cet algorithme ne fonctionne pas pour des graphes avec circuit.\n"+
        "\n"+
        "#cas 2 \n"+
        "Mauvais choix du sommet de départ."+"\n"
        +"L'algorithme bloque quand un sommet n'a pas de predecesseurs(sommet 0)"
        +"\n \n"
        "@solution"
         +"\n"+ "Utiliser Bellman2"+"\n")

######################################################
#### Extraire le plus court chemin entre deux sommets
#Si chemin existe on l'Affiche
#Sinon on envoie message d'erreur
####################################################

def BellmanXY(graphe, sm1,sm2):
    """
        param In : graphe, sommet source, sommet destination

        param out : liste =[ sm1, b, sm2] : chemin entre sm1 et sm2 si existe
                    cost : int : le cout du chemin
                        --
                     liste=[None] : si pas de chemin
                     cost = None  : ||
    """
    d,pred =pccBellman(graphe,sm1)

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

#####################################################
## Affiche tous les plus courts chemin
#    entre le sommet source et tous les autres sommets
#################

def Bellman(graphe,s):
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
            listd,cost=BellmanXY(graphe,s,sommet)
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
