#-*-coding:utf8-*-

import numpy as np




""" fonction qui prend en parametre
la matrice de distance et retourne les voisins"""

def voisins(matrice,sommet):
    """Entrées :
    Matrice de distances
    le sommet i
    
    Sortie:

    La liste de voisins
    """

    voisins=[]
    i=sommet
    j=0
    #print(len(matrice[i]))
    while j<len(matrice[i]):
        if matrice[i][j] not in [-1,0]:
            voisins.append(j)
        #print(j)
        j=j+1
    return voisins

"""
parametre input :
         matrice de distance = type matrice
         sommet = integer
Return :
       NOMBRE DE VOISINS = integer
       """
    
def degre(matrice,sommet):
    #appel de voisins
    degre=len(voisins(matrice,sommet))
    print("Le sommet {0} a {1} voisins".format(sommet,degre))


"""
parametre input :
      matrice de distance de G = type matrice
      liste de sommets de G = type list

Return :
     -1 SI Chemin pas possible
     longueur du chemin = type integer
     """
def longueur(matrice,L):
    pred=0
    suc=pred+1
    longueur=0
    estChemin = True
    while suc < len(L):
        if matrice[L[pred]][L[suc]] != -1:
            longueur=longueur + matrice[L[pred]][L[suc]]
            #print(longueur)
        else:
            estChemin=False
            break
        pred,suc=suc,suc+1
    ##fin de parcours de la boucle
    if estChemin==False:
        return -1
    else:
        return longueur

##############################

##fonction principal de test

#############################"



matrice=[[0,9,3,-1,7],
         [9,0,1,8,-1],
         [3,1,0,4,2],
         [-1,8,4,0,-1],
         [7,-1,2,-1,0]]
L=[1,2,0,4,2]
#print("liste des voisins du sommet 2".center(50,'-'))
#print(voisins(matrice,2))
#print("nombre de voisins sommet 2".center(50,'*'))
#degre(matrice,2)
print("calcul de longueur".center(50,'*'))
print(longueur(matrice,L))









"""fonction qui prend en parametre une matrice d'adjacence
et retourne une matrice de booleen"""

def matrice_bool(matrice_adjacence):
    i=0
    matrice_bool=[]
    for ligne_mat in matrice_adjacence:
        j=0
        m=[]
        for col_mat in ligne_mat:
            if matrice_adjacence[i][j]==0:
                m.append(False)
            else:
                m.append(True)
            j=j+1
        i=i+1
        matrice_bool.append(m)
    return matrice_bool

def affiche_matrice(matrice):
    for ligne_mat in matrice:
        print ligne_mat



    
###########################################
###
#Programme principal

#############################################


matrice_adjacence=[[0,1,0,1],
                   [1,0,0,0],
                   [1,0,0,0],
                   [0,0,0,0]]
matrice_bool=matrice_bool(matrice_adjacence)
#affiche_matrice(matrice_adjacence)
#affiche_matrice(matrice_bool)
m1=np.array(matrice_adjacence)
m2=np.dot(m1,m1)
print m1







                
            
    







