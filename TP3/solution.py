"""
Augustin Glemet/ Lilian saglibene
28/11/2022
fichier contenant une liste de mots que l'on appelera dans notre jeu du pendu

"""

from random import randint

def trie(solution):
    """
    fontion qui permet de classés les mots d'une liste par taille puis par ordre alphabétique
    entrée: liste de mot
    sortie: liste de mot triée
    """
    solution_alph = sorted(solution)
    solution_len = sorted(solution_alph,key=len)
  
    return(solution_len)
  
    
lst=["chat","souris","anticonstitutionnellement","interface","composants","application","carré"]

def mot_au_hasard():
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