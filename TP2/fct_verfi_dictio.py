#TP2
#réalisé le 21/11/2022
#Par Saglibene Lilian et Glemet Augustin 
#Objectif : Fonction qui renvoie si la phrase en entrée possède bien des mots du dictionnaire défnie.

from fct_trad_phrase import SaisirEntree

def verif_dictio(dictio, phrase) :
    """ 
    Entrée : - Le dictionnaire sur lequel on travaille (les mots permis) 
             - La phrase (string) que l'on traite
    Sortie : Nous renvoi un booléen pour savoir si tous les mots de notre phrase sont dans le dictionnaire
    """ 
    l_phrase = SaisirEntree(phrase)
    type_mot=[-1 for i in range(len(l_phrase))] #Initilisation du tableau des clés de chaque mot de notre phrase ( article : 0, nom : 1 ... ) (tab of int)
    for  i in range (len(l_phrase)) :
        for l_phrase[i] in dictio :
            if l_phrase[i] == dictio.values() :
                type_mot[i] = dictio.keys() 
            else :
                return 0
    return 1


