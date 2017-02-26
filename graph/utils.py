#-*-coding:utf8-*-


"""
Objet file dattente, pour la mise en oeuvre de FIFO
Fist In First Out : Premier entrée Premier Sortie, File d'attente
"""

class File_attente(object):
    """une file dattente mise en oeuvre avec liste"""
    def __init__(self):
        self.liste_attente=[]

    def ajout(self,element):
        self.liste_attente.append(element)

    def retirer(self):
        sortie = self.liste_attente[0]
        del self.liste_attente[0]
        return sortie

    def taille(self):
        return len(self.liste_attente)
    
