#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°3 : Objectif : Faire un programme qui calcule le montant des impôts d'une seule personne

from fct_impot import mesimpots
#Programme Main 

revenus = int(input("Saisissez le revenus que vous gagnez par an"))
print("Les impôts que vous devez payer s'élève à :", mesimpots(revenus),"€")

#avec 50000€ on retrouve le résultat de l'énoncé 
