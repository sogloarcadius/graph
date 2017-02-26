#-*-coding:utf8-*-

import graphe
from utils import File_attente


#################################################################

# Author : Arcadius SOGLO
# Licence : GPL

##################################################################

"""
==============Parcours du graphe en profondeur recursivement===============

===========================Algorithme==========
Procedure ParcoursProfondeur(Graphe, S)
Debut
    Si NotMarque(S):
        marque(S)
        traiter(S)
        Pour chaque successeurs S' de S:
            ParcoursProfondeur(Graphe, S')
        FPour
    FSi
Fin
"""


def Parcours_Profondeur(graphe,S):
    if S not in SommetTraiter:
        SommetTraiter.append(S)
        print(S)
    for T in graphe.successeurs(S):
        if T not in SommetTraiter:
            ParcoursProfondeur(graphe,T)

def ParcoursProfondeur(graphe,S):
    global SommetTraiter
    SommetTraiter=[]
    Parcours_Profondeur(graphe,S)



"""

============Parcours en largeur ==========================================
==================Algorithme================================================

Procedure ParcoursLargeur(graphe, S):

Initialisation
    file <-- fileVide()
    ajoutSommet(file,S)
Debut
    tant que NotVide(file):
        S_cour <-- retirerSommet(file)
        marquer(S_cour)
        traiter(S_cour)
        Pour chaque successeurs T de S_cour:
            if NotMarque(S_cour):
                ajoutSommet(file,T)
            FSi
        FPour
    FTQ
FIN

"""


def Parcours_Largeur(graphe,S):
    file = File_attente()
    file.ajout(S)
    while file.taille() != 0:
        S_cour = file.retirer()
        SommetTraiter.append(S_cour)
        print(S_cour)
        for T in graphe.successeurs(S_cour):
            if T not in SommetTraiter:
                file.ajout(T)

def ParcoursLargeur(graphe, S):
    global SommetTraiter
    SommetTraiter=[]
    Parcours_Largeur(graphe,S)





#####################################################################

#                       Fonction principale #

#####################################################################

g=graphe.Graphe([1,2,3,4,5,6,7,8],[(1,2),(1,3),(1,4),(2,5),(2,6),(3,6),(3,7),(6,8)])
#print(g.successeurs(1))
print("Parcours en Largeur".center(50,"*"))
ParcoursLargeur(g,1)
print("Parcours en profondeur".center(50,"*"))
ParcoursProfondeur(g,1)
