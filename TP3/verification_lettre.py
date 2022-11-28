"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Créer une fonction si la lettre proposé par l'utilisateur est dans le mot recherché

"""

def verif_lettre(lettre_prop, solution):
    lettre_sol=list(solution) 
    list_indice=[-1 for i in range(len(lettre_sol))]
    for i in range(len(lettre_sol)):
        if lettre_prop == lettre_sol[i]:
            list_indice[i]=i
    return list_indice
        
            