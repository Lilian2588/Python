"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : Fonction qui renvoie un booléen : si la liste (underscore) contient des underscores ou non.

"""

def aucun_tiret(liste):
    for i in range(1,len(liste)) :
        if liste[i]=="_" :
            return False 
    return True