#-*-coding:utf8

from Graphe import *
from Dijkstra import *

# @author :
	#Arcadius SOGLO
# @Description : Tests unitaires des algorithme des Dijkstra et Bellman Ford
	# On utilise Objet de type graphe, type abstrait de donnée pour manipuler les graphes
#@Warning :
	#On oblige des sommets entiers numeroté a partir de " 0 " pour optimisation de code
	#car mon implémentation de l'algorithme utilise les matrices d'adjacence pour faire le routage



# graphe = Graphe(6)
# graphe.Ajouter_arc(0,1,2,False)
# #graphe.Ajouter_arc(1,7,2,False)####arrete deja dans le graphe, juste au dessus, test OK !
# graphe.Ajouter_arc(0,3,4,False)
# graphe.Ajouter_arc(0,2,5,False)
# graphe.Ajouter_arc(1,2,2,False)
# graphe.Ajouter_arc(3,2,1,False)
# graphe.Ajouter_arc(1,4,7,False)
# graphe.Ajouter_arc(2,4,4,False)
# graphe.Ajouter_arc(2,5,3,False)
# graphe.Ajouter_arc(4,5,1,False)
# graphe.Ajouter_arc(4,6,5,False)
# graphe.Ajouter_arc(5,6,7,False)
#
# DijkstraXY(graphe,6,5)

# graphed = Graphe(4)
# graphed.Ajouter_arc(0,1,10)
# graphed.Ajouter_arc(0,3,30)
# graphed.Ajouter_arc(0,4,100)
# graphed.Ajouter_arc(1,2,50)
# graphed.Ajouter_arc(3,2,20)
# graphed.Ajouter_arc(3,4,60)
# graphed.Ajouter_arc(2,4,10)
# Dijkstra(graphed,0)
# print()
# print()
# Dijkstra2(mg,1,4)


graphed = Graphe(7)
graphed.Ajouter_arc(0,7,4)
graphed.Ajouter_arc(0,4,4)
graphed.Ajouter_arc(0,1,4)
graphed.Ajouter_arc(1,3,4)
graphed.Ajouter_arc(2,6,4)
graphed.Ajouter_arc(2,1,4)
graphed.Ajouter_arc(2,4,4)
graphed.Ajouter_arc(3,0,2)
graphed.Ajouter_arc(5,2,2)
graphed.Ajouter_arc(6,1,2)
graphed.Ajouter_arc(7,5,2)
Dijkstra(graphed,3)
