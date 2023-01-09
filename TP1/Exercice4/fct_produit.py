#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°4 : Objectif : calculer la mutiplication de deux matrice de tailles différentes si c'est possible

#fonction qui renvoie le produit de deux matrice 3x3 


from fct_init_array import init_array


def mult_matrice_carre(A,B):
    C=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (len(C)):
        for j in range(len(C)):
            for k in range(len(C)):
                C[i][j]+=A[i][k]*B[k][j]
    return C

#fonction qui renvoie le produit de deux matrice si le format de celles-ci est compatible  

def mult_matrice(A,B):
    if len(A[0])==len(B):
        C=init_array(len(A),len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    C[i][j]+=A[i][k]*B[k][j]
        return C






