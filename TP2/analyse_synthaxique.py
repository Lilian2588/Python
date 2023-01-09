#TP2
#réalisé le 21/11/2022
#Par Saglibene Lilian et Glemet Augustin 
#Objectif : Analyse grammaticale de la phrase et retourne si la phrase est correcte ou non 

from fct_trad_phrase import SaisirEntree
from fct_verfi_dictio import verif_dictio
from fct_action_selon_sortie import ActionSortie

def analyse_synthax(tab_tr, phrase, dictio) :
    """ 
    Entrée : - Le tableau de transistion(liste de listes) qui résume les états selon les entrées
             - La phrase (chaine de caractère) que l'on traite
             - Le dictionnaire( dictionnaire) sur lequel on se base
    Sortie : Analyse la synthaxe de la phrase 
    """ 
    if verif_dictio(dictio,phrase) == 1 :  
        etat=0
        l_phrase=SaisirEntree(phrase)
        for  i in range (len(l_phrase)) : 
            mot=l_phrase[i]
            type_mot=dictio[mot]  #Initilisation du tableau des clés de chaque mot de notre phrase ( article : 0, nom : 1 ... ) (tab of int)

            while (etat < 9) : 
                etat=tab_tr[etat][type_mot]
                if (etat == 8) :
                    return(ActionSortie(etat))
            return (ActionSortie(etat))
    else : 
        return(ActionSortie(8))


