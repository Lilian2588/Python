"""
Augustin Glemet/ Lilian saglibene
28/11/2022
fichier qui contient la fonction permetttant de choisir un mot au hasard dans une liste
"""
from solution import trie
from random import randint
def mot_au_hasard(lst):
    """
    fonction qui permet de renvoyer un mot de notre liste au hasard
    entrée= none
    sortie: liste de caractère
    """
    mot = trie(lst)
    i = randint(0,len(mot)-1)
    mot_au_hasard = mot[i]
    return(mot_au_hasard)
    
print (mot_au_hasard())
