"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Créer une fonction si la lettre proposé par l'utilisateur est dans le mot recherché

"""

def verif_lettre(lettre_pro, solution):
    list_indice=[]
    lettre_sol=list(solution) 
    for i in range(len(lettre_sol)-1):
        if lettre_pro == lettre_sol[i]:
            list_indice[i] = i 
        else :
            return("Perdu, la lettre n'est pas présente dans le mot")
    return list_indice
        
            