"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : création du Pendu sans interface graphique

"""

from replace_blank import replace_blank
from verification_lettre import verif_lettre 
from est_vide import est_vide
from ens_sol import mot
from aucun_underscore import aucun_tiret

#On import le mot depuis le fichier où on stocke notre ensemble mots
solution = mot
print(solution)

#On affiche la première lettre du mot
letter = list(solution)
print(len(letter))
#On affiche des "underscore" pour cacher le mot
underscore=[]
underscore.append(letter[0])
for i in range (1, len(letter)) : 
    underscore.append("_")

erreur = 0
while erreur != 8 and not(aucun_tiret(underscore)) :
    print(underscore)
    prop_lettre = input("Proposer une lettre") 
    print(verif_lettre(prop_lettre, solution))
    if est_vide(verif_lettre(prop_lettre, solution)) :
        erreur += 1
    else : 
        underscore = replace_blank(underscore, prop_lettre, solution)
    print(underscore)






