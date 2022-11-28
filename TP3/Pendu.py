"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : création du Pendu sans interface graphique

"""

from solution import mot_au_hasard

solution = mot_au_hasard()

#On affiche la première lettre du mot
letter = list(solution)
print(letter[0])
#On affiche des "underscore" pour cacher le mot
underscore=[]
underscore[0]=letter[0]
for i in range (1, len(solution)-1) : 
    underscore[i] = "_"

prop_lettre = input("Entrer une lettre")




