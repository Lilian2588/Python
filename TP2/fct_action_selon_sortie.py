#TP2
#réalisé le 21/11/2022
#Par Saglibene Lilian et Glemet Augustin 
#Objectif : Affichage du résultat 

def ActionSortie(s):
    """ 
    Entrée : La valeur de notre état (int) de transition 
    Sortie : Affiche si la phrase est correcte ou non (str)
    """ 
    if s==8 :
        return("La phrase est incorrecte.")
    else :
        return ("La phrase est correcte.")