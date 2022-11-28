"""
Augustin Glemet/ Lilian saglibene
28/11/2022
fichier contenant une liste de mots que l'on appelera dans notre jeu du pendu

"""

def trie(solution):
    """
    fontion qui permet de classés les mots d'une liste par taille puis par ordre alphabétique
    entrée: liste de mot
    sortie: liste de mot triée
    """
    solution_alph = sorted(solution)
    solution_len = sorted(solution_alph,key=len)
  
    return(solution_len)
