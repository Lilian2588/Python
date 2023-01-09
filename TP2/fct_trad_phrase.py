#TP2
#réalisé le 21/11/2022
#Par Saglibene Lilian et Glemet Augustin 
#Objectif : Traduire une phrase sous forme de liste.


def SaisirEntree(phrase) :

    """
    Entrées : La phrase que l'on traite (str)
    Sortie : Convertit notre phrase en liste de chaines de caractères
    """
    tab = phrase.split()
    for i in range(len(tab))  : 
        tab[i].split(".") 
    return tab
