"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : création du Pendu 

"""
from jeu import pendu 
from replay import replay

#Lancement du jeu
rejouer = True 
while rejouer == True :
    pendu()
    rejouer = input("Voulez-vous rejouez ? y/n")
    rejouer = replay(rejouer)
