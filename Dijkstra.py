#! /usr/bin/python3
#-*-coding:utf8-*-

from Graphe import *

############################################################
#Implementation de l'algorithme de Dijkstra
#Author : SOGLO Arcadius
#Python 3.4.2
#####################################################


##fonction pour calculer les plus court chemin avec la matrice d'adjacence
##Applique algorithme de Dijkstra
def pccDijkstra(mg,s):

    """
    arguments : mg - matrice d'adjacence du graphe pondéré
                s - sommet d'originie
                les sommets sont des entiers naturels
    sortie : s_connu - dictionnaire { sommet : [longeur, plus court chemin ]}
    """
    # initialisation -----------------------------------

    infini = sum(sum(ligne) for ligne in mg)+1  ### somme des poids des arcs du graphe + 1
    nb_sommets =len(mg)


    s_connu = { s : [0,[s]]} #[longueur, plus court chemin]
    s_inconnu = { k : [infini, ''] for k in range(nb_sommets) if k != s}
                                #[longueur , precedent]
    for suivant in range(nb_sommets):
        if(mg[s][suivant]):
            s_inconnu[suivant] =[mg[s][suivant], s]
    # print("Dans le graphe d\'origine {} de matrice d\'adjacence".format(s))
    # for ligne in mg:
    #     print(ligne)
    # print()
    print('*'*50)
    print("Recherche du plus court chemin entre {} et tous les autres sommets".format(s))
    print("*"*50)
    print('Plus courts chemin de : ')

    ##---La Recherche des plus court chemin------------------------------
    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        u = min(s_inconnu, key = s_inconnu.get)
        longueur_u, precedent_u = s_inconnu[u]
        for v in range(nb_sommets):
            if mg[u][v] and v in s_inconnu:
                d=longueur_u + mg[u][v]
                if d < s_inconnu[v][0]:
                    s_inconnu[v] = [d,u]
        s_connu[u] = [ longueur_u, s_connu[precedent_u][1] + [u]]
        del s_inconnu[u]
        print('longueur', longueur_u, ' :', '->'.join(map(str,s_connu[u][1])))

    for k in s_inconnu:
        print("il ny a aucun chemin de {} à {} ".format(s,k))

    return s_connu


########################################################
#Utilise fonction PlusCourtChemins(pccDijkstra)
##Effectue les test de conditions d'application de l'algorithme
#########################################################

def Dijkstra(graphe,s):
    """
    arguments :
            graphe - Objet de type Graphe
            s - sommet d'origine

    sortie : affichage ergonomique des plus court chemin de {s} vers tous les autres sommets
    """
    if not graphe.Arc_negatif():#Dijkstra ne peut s'effectuer que si il n'y a aucun arc négatif
        if s in graphe.sommets: ##On vérifie existence du sommet dans la liste de sommet
            mg=graphe.Matrice()#on genere la matrice d'adjacence de l'objet graphe creé
            pccDijkstra(mg,s) ## retourne dictionnaire { sommet : [longeur, plus court chemin ]
        else:
            print("Le sommet n'existe pas".center(50,"*"))
    else :
        print("Dijkstra ne peut s'effectuer que si il n'y a aucun arc négatif")


######################################################################################"

#Calcul du plus court chemin entre deux sommets X et Y

#On extrait de notre dictionnaire précedent le plus court chemin entre ces deux sommet si chemin existe
#
#sinon on affiche pas de chemin entre les deux sommets
######################################################################################"

def pccDijkstraXY(mg,s,g):
    """
    arguments : mg - matrice d'adjacence du graphe pondéré
                s - sommet d'origine
                g - sommet à atteindre(objectif)
                les sommets sont des entiers naturels
    sortie : s_connu - dictionnaire { sommet : [longeur, plus court chemin ]}
    """
    # initialisation -----------------------------------

    infini = sum(sum(ligne) for ligne in mg)+1
    nb_sommets =len(mg)

    s_connu = { s : [0,[s]]} #[longueur, plus court chemin]
    s_inconnu = { k : [infini, ''] for k in range(nb_sommets) if k != s}
                                #[longueur , precedent]
    for suivant in range(nb_sommets):
        if(mg[s][suivant]):
            s_inconnu[suivant] =[mg[s][suivant], s]
    # print("Dans le graphe d\'origine {} de matrice d\'adjacence".format(s))
    # for ligne in mg:
    #     print(ligne)
    print("*"*50)
    print("Recherche du plus court chemin entre {} et {}".format(s,g))
    print("*"*50)

    ##---La Recherche des plus courts chemin ------------------------------
    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        u = min(s_inconnu, key = s_inconnu.get)
        longueur_u, precedent_u = s_inconnu[u]
        for v in range(nb_sommets):
            if mg[u][v] and v in s_inconnu:
                d=longueur_u + mg[u][v]
                if d < s_inconnu[v][0]:
                    s_inconnu[v] = [d,u]
        s_connu[u] = [ longueur_u, s_connu[precedent_u][1] + [u]]
        del s_inconnu[u]
    if g in s_connu:
        print("Plus courts chemin de longueur {} -> {}".format(s_connu[g][0],s_connu[g][1]))
    else :
        print("il ny a aucun chemin de {} à {} ".format(s,g))

######################################################
#### Extraire le plus court chemin entre deux sommets
#Si chemin existe on l'Affiche
#Sinon on envoie message d'erreur

def DijkstraXY(graphe,s,g):
    """
    arguments :
            graphe - Objet de type Graphe
            s - sommet d'origne (depart X)
            g - sommet à atteindre (Arrivée Y)

    sortie : affichage ergonomique du plus court chemin entre {s} et {g}
    """
    if not graphe.Arc_negatif():#Dijkstra ne peut s'effectuer que si il n'y a aucun arc négatif
        if s in graphe.sommets and g in graphe.sommets: ##On vérifie existence du sommet dans la liste de sommet
            mg=graphe.Matrice()#on genere la matrice d'adjacence de l'objet graphe
            pccDijkstraXY(mg,s,g) ## retourne dictionnaire { sommet : [longeur, plus court chemin ]
        else:
            print("Un des sommets n'existe pas".center(50,"*"))
    else :
        print("Dijkstra ne peut s'effectuer que si il n'y a aucun arc négatif")
