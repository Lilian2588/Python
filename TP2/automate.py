#TP2
#réalisé le 21/11/2022
#Par Saglibene Lilian et Glemet Augustin 
# Objectif : Créer un automate pour reconnaître si une phrase est syntaxement correct. 
# To do : 
#   - Implémenter d'un type (enregistrement) phrase 
#   - Créer une fonction qui prend en entré une phrase et qui traduit (renvoie) en une table d'entrée. 
#   - Création d'une fonction qui dis si une phrase est correct grammaticalement. 



from fct_trad_phrase import SaisirEntree
from fct_action_selon_sortie import ActionSortie
from analyse_synthaxique import analyse_synthax

#Programme principal 

dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

#Phrases correctes
phrase1 = "Le joli chat joue."
phrase2 = "le ,joli chat ; joue."
phrase3 = "la grosse souris verte mange le joli petite chat blanc ."
phrase4 = "la grosse souris verte mange jean."
phrase5 ="Jean joue ."

#Phrases incorrectes 
phrase6="."
phrase7=""
phrase8 ="le joli chat joue"

#table d'états de transition.


table_tr=[
 [1,8,8,8,4,8]
,[8,1,2,8,8,8]
,[8,2,8,3,8,8]
,[5,8,8,8,7,9]
,[8,8,8,3,8,8]
,[8,5,6,8,8,8]
,[8,6,8,8,8,9]
,[8,8,8,8,8,9]
]
print(table_tr)

#Affichage
print(SaisirEntree(phrase2))
print(SaisirEntree(phrase6))
l1 = SaisirEntree(phrase3)

print(analyse_synthax(table_tr,phrase3,dictionnaire))

