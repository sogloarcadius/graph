#-*-coding:utf8-*-

# @author :
	#Arcadius SOGLO
# @Description : TAD pour les graphes
	# Objet de type graphe, type abstrait de donnée pour manipuler les graphes
#@Warning :
	#On oblige des sommets entiers numeroté a partir de " 0 "
	#car algorithme utilise les matrices d'adjacence pour les calculs

class Graphe(object):

	def __init__(self,n):
		self.arcs ={} # dictionnaire des arcs du graphe
		self.sommets=[] # liste des sommets du graphe
		if isinstance(n,int): # n est un int, il y aura n sommet de valeur 0 à n
			for i in range(n+1):
				self.sommets.append(i)
		elif isinstance(n,list): # n est une liste qu'on place dans sommet directement
			for i in range(len(n)):
				self.sommets.append(n[i])
		else:
			print("Votre paramètre d'entrée n'est pas compatible".center("@",50))

	# Ajoute de sommet si il n'existe pas déja dans le graphe
	#  Verification de la cohérence.(sommet type en entier)
	def Ajouter_sommet(self,sommet):
		if sommet not in self.sommets:
			if isinstance(sommet,int):
				self.sommets.append(sommet)
			else:
				print ("Sommet "+str(sommet)+" n'est pas compatible avec le graphe" )
		else:
			print("Le sommet existe déja")

	# Permet d'ajouter un arc au graphe si les deux sommets placé en paramètre existent et si l'arc n'existe pas déja.
	def Ajouter_arc(self, sm1, sm2, v=1, oriente=True):
		if sm1 in self.sommets and sm2 in self.sommets:
			if isinstance(sm1,int) and isinstance(sm2,int):
				if not (sm1,sm2) in self.arcs:
					self.arcs[(sm1,sm2)]=v
					if oriente == False:
						if not (sm2,sm1) in self.arcs:
							self.arcs[(sm2,sm1)]=v
				else:
					print (" Arc ou Arrete existe déja".center(50,'?'))
			else:
				print ("Sommet n'est pas compatible avec le graphe".center(50,'?') )
		else:
			print("Au moins 1 des deux sommets n'existe pas".center(50,'?'))

	def predecesseurs(self,sm):
		pred=[]
		for couple in self.arcs.keys():
			if couple[1]==sm:
				pred.append(couple[0])
		return pred

	def successeurs(self,sm):
		suc=[]
		for couple in self.arcs.keys():
			if couple[0]==sm:
				suc.append(couple[1])
		return suc



	# Cette fonction permet de générer la matrice lié au graphe. Servira pour djisktra
	#Condition importante : Sommet numerotée a partir de 0
	def Matrice(self):
		matrice=[[0 for x in range(len(self.sommets))] for x in range(len(self.sommets))]
		for key in self.arcs.keys():
			matrice[key[0]][key[1]]=self.arcs[(key[0],key[1])]
		return matrice

	# Affiche la matrice généré par Matrice() dans la console
	def AfficheMatrice(self):
		matrice = self.Matrice()
		for row in matrice:
			print(row)
			#print (" ".join(str(row)))

	# test si le graphe possède ou non des arcs négatifs
	def Arc_negatif(self):
		result=False
		for value in self.arcs.values():
			if value<0:
				result= True
		return result
