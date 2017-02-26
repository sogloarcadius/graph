#! /usr/bin/python3
#-*-coding:utf8


from graph.graphe import *
from graph.dijkstra import *
from graph.bellman import *
from graph.bellman2 import *
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

###Creation d'un graphe orienté g1
print("Création du graphe g1".center(50,"*"))
g1 = Graphe(4)
g1.Ajouter_arc(0,1,10)
g1.Ajouter_arc(0,3,30)
g1.Ajouter_arc(0,4,100)
g1.Ajouter_arc(1,2,50)
g1.Ajouter_arc(3,2,20)
g1.Ajouter_arc(3,4,60)
g1.Ajouter_arc(2,4,10)

print()
print()
print("successeurs du sommet 0 dans g1".center(50,"*"))
print(g1.successeurs(0))
print()

print()
print("predecesseurs du sommet 4 dans g1".center(50,"*"))
print(g1.predecesseurs(4))
print()

print("Matrice du graphe g1".center(50,"*"))
print()
g1.AfficheMatrice()
print()


####creation d'un graphe non orienté g2
print()
print("Création du graphe g2".center(50,"*"))
print()
g2 = Graphe(6)
g2.Ajouter_arc(0,1,2,False)
g2.Ajouter_arc(1,7,2,False)###sommet 7 n'existe pas(message d'erreur)
g2.Ajouter_arc(1,0,2,False)####arrete deja dans le graphe,(message d'erreur)
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

print()
print("Matrice du graphe g2".center(50,"*"))
print()
g2.AfficheMatrice()
print()

##################### Tests de djisktra #############################

print("Test de Dijkstra sur g1 avec sommet source 0".center(50,"*"))
print()
Dijkstra(g1,0)
print()
print("Test de Dijkstra sur g1 avec sommet source 1".center(50,"*"))
print()
Dijkstra(g1,1)
print()

print("Test de Dijkstra sur g2 avec sommet source 0".center(50,"*"))
print()
Dijkstra(g2,0)
print()

print("Afficher le pcc entre deux sommets avec Dijkstra dans g2".center(50,"*"))
print()
DijkstraXY(g2,0,2)
print()

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

print("creation du graphe g4".center(50,"*"))
print()
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
print()


print("creation du graphe g5".center(50,"*"))
print()
g5=Graphe(5)
g5.Ajouter_arc(0,2,5)
g5.Ajouter_arc(0,3,6)
g5.Ajouter_arc(0,1,4)
g5.Ajouter_arc(1,2,-3)
g5.Ajouter_arc(2,5,4)
g5.Ajouter_arc(3,4,2)
g5.Ajouter_arc(4,5,2)
g5.Ajouter_arc(5,4,1)
#g5.Ajouter_arc(5,4,-4)
print()


print("Test de Dijkstra sur g4 et g5 mais erreur ".center(50,"*"))
#erreur car Dijkstra ne fonctione pas avec des arcs negatifs
print()
Dijkstra(g4,0)
Dijkstra(g5,1)
print()

print("Test de Bellman sur g4(pas de circuit)".center(50,"*"))
print()
Bellman(g4,0)
print()

print("Test de Bellman2 sur g5(circuit)".center(50,"*"))
print()
Bellman2(g5,0)

# print("Test de Bellman sur g5(circuit)".center(50,"*"))
# print()
# Bellman(g5,0)
# print()
