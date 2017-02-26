#! /usr/bin/python3
#-*-coding:utf8-*-



# implementation avec de la programmation objets









# implementation des arbres avec des listes

"""
   voici la Structure de notre Arbre

   [valeur,[fils_gauche],[fils_droit]]
"""
def est_vide(a):
    "retourne True si a est vide et False sinon"
    if len(a)==0:
        return True
    else:
        return False


def fils_gauche(a):
    "retourne le fils gauche de a si a est non vide et rien sinon"
    if len(a) !=0:
        return a[0]

def fils_droit(a):
    if len(a) !=0:
        return [2]

def insertion(v,a):
    if v not in a:
        a.append(v)

def insertion_liste(lv,a):
    """insere les valeurs de la liste lv dans a qui
n’y figurent pas deja."""
    for value in lv:
        if value not in a:
            a.append(value)


###affiche les valeurs selon le mode précisé
def afficher(a,mode):
    """
mode peut prendre les valeurs prefixe, infixe,postfixe
    """
    if mode==prefixe:





