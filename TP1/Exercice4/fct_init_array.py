#TP1
#réalisé le 16/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°4 : Objectif : initialiser un tableau de sous tableaux (matrice)

def init_array(n,p):
    arr=[]
    for i in range(n):
        arr.append([0 for i in range(p)])
    return arr
