#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°2 : Objectif : établir un programme pour voir si une année est bissextile ou non

from fct_calendrier import est_bissextile
from fct_calendrier import nombre_jour
from fct_calendrier import est_valide

#4)
#Programme Main 
#variables pour tester les fonctions
date1  = 1589
date2 = 1304
#test des fonctions 
print("L'année est bissextile :", est_bissextile(date1))
print("L'année est bissextile :", est_bissextile(date2))
print("Le nombre de jours de cette date est", nombre_jour(date1,2))
print("Le nombre de jours de cette date est", nombre_jour(date2,2))


#interraction avec l'utilisateur 
jour = int(input("Veuiller saisir un jour valide svp ?"))
mois = int(input("Veuiller saisir un mois valide svp ?"))
annee = int(input("Veuiller saisir une année valide svp ?"))

print("La date est valide :", est_valide(jour,mois,annee))






