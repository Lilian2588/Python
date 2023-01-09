"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Fonction qui préviens l'utilisateur si la lettre à déjà été écrit

"""
def lettre_deja_ecrit(prop_lettre, lettre_used) :
    for i in range (len(lettre_used)) : 
        if prop_lettre == lettre_used[i] :
            return("La lettre a déjà été utilisée frérot")
    lettre_used.append(prop_lettre)
    return("")