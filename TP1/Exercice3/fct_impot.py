#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°3 : Objectif : Faire un programme qui calcule le montant des impôts d'une seule personne

# On calcule la fonction avec en paramètre les revenus par an d'une seule personne et renvoie le montant des impôts qui devra payer 
# Chaque condition représente chaque cas du tableau 

#Import de la fonction qui renvoie la partie entière d'un réel 
from math import floor 

def mesimpots(revenus):
    if revenus <= 10225:
        return 0
    else:
        if revenus <= 26070:
            (revenus - 10225)*11/100
        else :
            if revenus <= 74545:
                rep = (revenus - 26071)*30/100
                rep = rep + (26070 - 10225)*11/100
                return floor(rep) 
            else :
                if revenus <= 160336:
                    rep = (revenus - 74546)*41/100
                    rep = rep + (74545 - 26071)*30/100
                    rep = rep + (26070 - 10225)*11/100
                    return floor(rep) 
                else :
                    rep = (revenus - 160337)*45/100
                    rep = rep + (160336 - 74546)*41/100
                    rep = rep + (74545 - 26071)*30/100
                    rep = rep + (26070 - 10225)*11/100
                    return floor(rep)