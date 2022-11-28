"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Créer une fonction pour remplacer les underscore par la lettre

"""

from est_vide import est_vide 
from verification_lettre import verif_lettre


def replace_blank(underscore, lettre_prop, solution) :
    """
        entrées : - underscore(liste) qui représente à la base une liste de underscore
                  - lettre_prop (str) qui représente la lettre que propose l'utilisateur
                  - solution (str) qui représente la solution du pendu
        sortie : renvoie une liste ( underscore) ou les underscore correspondant seront remplacés par les lettres(correctes)

    """
    if not(est_vide(verif_lettre(lettre_prop, solution))) : 
        for i in range(len(verif_lettre(lettre_prop, solution))) : 
            if verif_lettre(lettre_prop, solution)[i] == i :
                underscore[i] = lettre_prop
    else :
        return
    return underscore