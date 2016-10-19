#-*-coding:utf8

from Graphe import *
from Dijkstra import *
from Bellman import *

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



##################### Tests de djisktra #############################
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
##Dijkstra(graphed,3)



##################### Tests de Bellman #############################

grapheb= Graphe(5)
grapheb.Ajouter_arc(0,1,1)
grapheb.Ajouter_arc(0,2,-2)
grapheb.Ajouter_arc(1,3,-2)
grapheb.Ajouter_arc(1,5,3)
grapheb.Ajouter_arc(2,1,1)
grapheb.Ajouter_arc(2,3,5)
grapheb.Ajouter_arc(2,4,4)
grapheb.Ajouter_arc(4,5,-1)
grapheb.Ajouter_arc(5,3,-5)
#Bellman(grapheb,0)

####deuxieme test

graphec=Graphe(5)
graphec.Ajouter_arc(0,3,6)
graphec.Ajouter_arc(0,2,5)
graphec.Ajouter_arc(0,1,4)
graphec.Ajouter_arc(1,2,-3)
graphec.Ajouter_arc(2,5,4)
graphec.Ajouter_arc(3,4,2)
graphec.Ajouter_arc(4,5,2)
graphec.Ajouter_arc(5,4,1)

# s_connu =[0]
# s_inconnu=[1,2,3,4,5]
#
# print(choisir(graphec,s_inconnu,s_connu))
print(BellmanXY2(grapheb,0,1))
