"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Créer une fonction qui renvoie si une liste est vide ou non


"""
def est_vide(L) : 
    if len(L) == 0 : 
        return True
    for i in range(len(L)) : 
        if L[i] != -1  :
            return False 
    return True 
    
