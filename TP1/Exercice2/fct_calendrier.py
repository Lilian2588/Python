#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°2 : Objectif : établir un programme pour voir si une année est bissextile ou non


#1) renvoie si une année est bissextile 
def est_bissextile(annee):
    if (annee%4 == 0 and annee%100!=0) or (annee%400==0):
        return True
    else :
        return False

#2) renvoie le nombre de jours du mois choisis
def nombre_jour(annee,mois):
    if (mois == 1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
        return 31
    else :
        if (mois == 2):
            if(est_bissextile(annee)):
                return 29
            else:
                return 28
        else:
            return 30
#3) renvoie si une date est valide 
def est_valide(jour, mois, annee):
    if annee >= 1582 and jour <= 31 and mois <= 12 :
        if mois == 2 :
            if (nombre_jour(annee,mois) == 29 and est_bissextile(annee) and jour <=29) or (nombre_jour(annee,mois) == 28 and est_bissextile(annee) == False and jour<=28) :
                return True
        else :
            if nombre_jour(annee,mois) == 30 or nombre_jour(annee, mois) == 31 :
                return True
    return False 
    
