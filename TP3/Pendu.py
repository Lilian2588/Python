"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : création du Pendu sans interface graphique

"""

from replace_blank import replace_blank
from ens_sol import mot

#On import le mot depuis le fichier où on stocke notre ensemble mots
solution = mot
print(solution)

#On affiche la première lettre du mot
letter = list(solution)
print(len(letter))
#On affiche des "underscore" pour cacher le mot
underscore=[]
underscore.append(letter[0])
for i in range (1, len(solution) - 1) : 
    underscore.append("_")

for i in range(1, 8):
    for i in range(0, len(letter)-1):
        print(underscore[i])
    prop_lettre = input("Proposer une lettre")
    underscore = replace_blank(underscore, prop_lettre, solution)








