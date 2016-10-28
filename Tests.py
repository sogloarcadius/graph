#! /usr/bin/python3
#-*-coding:utf8

from Graphe import *
from Dijkstra import *
from Bellman import *
from Bellman2 import *
# @author :
	#Arcadius SOGLO
# @Description : Tests unitaires des algorithme des Dijkstra et Bellman
	# On utilise Objet de type graphe, type abstrait de donnée pour manipuler les graphes
"""
@Warning :
	#On oblige des sommets entiers numeroté a partir de " 0 "
	#car mon implémentation de l'algorithme utilise les matrices d'adjacence pour faire le routage
"""

##################### Tests du TAD #############################

###Creation d'un graphe orienté

g1 = Graphe(4)
g1.Ajouter_arc(0,1,10)
g1.Ajouter_arc(0,3,30)
g1.Ajouter_arc(0,4,100)
g1.Ajouter_arc(1,2,50)
g1.Ajouter_arc(3,2,20)
g1.Ajouter_arc(3,4,60)
g1.Ajouter_arc(2,4,10)


# print()
# print("successeurs du sommet 0".center(50,"*"))
# print(g1.successeurs(0))
# print()

# print()
# print("predecesseurs du sommet 4".center(50,"*"))
# print(g1.predecesseurs(4))
# print()

#g1.AfficheMatrice()

####creation d'un graphe non orienté

g2 = Graphe(6)
g2.Ajouter_arc(0,1,2,False)
#g2.Ajouter_arc(1,7,2,False)###sommet 7 n'existe pas(message d'erreur)
#g2.Ajouter_arc(1,0,2,False)####arrete deja dans le graphe,(message d'erreur)
g2.Ajouter_arc(0,3,4,False)
g2.Ajouter_arc(0,2,5,False)
g2.Ajouter_arc(1,2,2,False)
g2.Ajouter_arc(3,2,1,False)
g2.Ajouter_arc(1,4,7,False)
g2.Ajouter_arc(2,4,4,False)
g2.Ajouter_arc(2,5,3,False)
g2.Ajouter_arc(4,5,1,False)
g2.Ajouter_arc(4,6,5,False)
g2.Ajouter_arc(5,6,7,False)

#g2.AfficheMatrice()


##################### Tests de djisktra #############################


#Dijkstra(g1,0)
#Dijkstra(g1,1)

#Dijkstra(g2,0)
#DijkstraXY(g2,0,2)


# g3 = Graphe(7)
# g3.Ajouter_arc(0,7,4)
# g3.Ajouter_arc(0,4,4)
# g3.Ajouter_arc(0,1,4)
# g3.Ajouter_arc(1,3,4)
# g3.Ajouter_arc(2,6,4)
# g3.Ajouter_arc(2,1,4)
# g3.Ajouter_arc(2,4,4)
# g3.Ajouter_arc(3,0,2)
# g3.Ajouter_arc(5,2,2)
# g3.Ajouter_arc(6,1,2)
# g3.Ajouter_arc(7,5,2)
# #Dijkstra(g3,0)
# #DijkstraXY(g3,6,0)


##################### Tests de Bellman #############################

g4= Graphe(5)
g4.Ajouter_arc(0,1,1)
g4.Ajouter_arc(0,2,-2)
g4.Ajouter_arc(1,3,-2)
g4.Ajouter_arc(1,5,3)
g4.Ajouter_arc(2,1,1)
g4.Ajouter_arc(2,3,5)
g4.Ajouter_arc(2,4,4)
g4.Ajouter_arc(4,5,-1)
g4.Ajouter_arc(5,3,-5)


g5=Graphe(5)
g5.Ajouter_arc(0,2,5)
g5.Ajouter_arc(0,3,6)
g5.Ajouter_arc(0,1,4)
g5.Ajouter_arc(1,2,-3)
g5.Ajouter_arc(2,5,4)
g5.Ajouter_arc(3,4,2)
g5.Ajouter_arc(4,5,2)
#g5.Ajouter_arc(5,4,1)
g5.Ajouter_arc(5,4,-4)

#erreur car Dijkstra ne fonctione pas avec des arcs negatifs
#Dijkstra(g4,0)
#Dijkstra(g5,1)

#Bellman(g4,0)
#Bellman(g5,0)

Bellman2(g5,0)
