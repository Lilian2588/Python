"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Fonction qui préviens l'utilisateur si la lettre à déjà été écrit

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
