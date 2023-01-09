"""
    TP3
    réalisé le 28/11/2022
    Par Saglibene Lilian et Glemet Augustin 
    Objectif : création du Pendu sans interface graphique

"""


from replace_blank import replace_blank
from verification_lettre import verif_lettre 
from est_vide import est_vide
from aucun_underscore import aucun_tiret
from lettre_deja_ecrit import lettre_deja_ecrit
from random_word import mot_au_hasard



def pendu() :
    #Tableau des scores
    score=[]
    #On import le mot depuis le fichier où on stocke notre ensemble mots
    #solution = mot_au_hasard(open('mots.txt','r'))
    solution = mot_au_hasard(lst)
    print(solution)
    #On affiche la première lettre du mot
    letter = list(solution)
    #print(len(letter))
    #On affiche des "underscore" pour cacher le mot
    underscore=[]
    underscore.append(letter[0])
    for i in range (1, len(letter)) : 
        underscore.append("_")
    #On crée un tableau des lettres utilisés par l'utilisateur
    lettre_used = ["" for i in range (26)]
    #erreur (tentative < 9 )  
    erreur = 0
    #nb de tentatives 
    tentative = 0
    while erreur != 8 and not(aucun_tiret(underscore)) :
        print(underscore)
        prop_lettre = input("Proposez une lettre")
        tentative += 1
        print(lettre_deja_ecrit(prop_lettre, lettre_used))
        #print(verif_lettre(prop_lettre, solution))
        if est_vide(verif_lettre(prop_lettre, solution)) :
            erreur += 1
        else : 
            underscore = replace_blank(underscore, prop_lettre, solution)
    if est_vide(verif_lettre(prop_lettre, solution)) :
        print("Perdu :(")
    else : 
        print(">>> Gagner le boss <<<")
    ratio = (len(letter)*100)//(tentative + erreur)
    score.append("(nb lettres =")
    score.append(len(letter))
    score.append(";")
    score.append('fautes :') 
    score.append(erreur)
    score.append(';')
    score.append('tentatives :')
    score.append(tentative)
    score.append(';')
    score.append('ratio :')
    score.append(ratio)
    score.append('%)---')
    print(score)
    print(underscore)