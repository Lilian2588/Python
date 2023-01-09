#TP1
#réalisé le 14/11/2022
#Par Saglibene Lilian 
#Faire l'exercice n°4 : Objectif : calculer la mutiplication de deux matrice de tailles différentes si c'est possible

            
from random import *

from fct_init_array import init_array
#Programme Main 
from fct_produit import mult_matrice, mult_matrice_carre

#initialisation des tableaux
A=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range (len(A)):
        A[i][j]=randint(1,4)
print("Le tableau A est :", A)
B=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(B)):
    for j in range (len(B)):
        B[i][j]=randint(1,4)
print("Le tableau B est :", B)

print("Voici la multiplication de A par B:", mult_matrice_carre(A,B))

#produit de matrice quelconques
A=init_array(3,2)
for i in range(len(A)):
    for j in range (len(A[0])):
        A[i][j]=randint(1,4)
print("Le tableau A est :", A)

B=init_array(2,4)
for i in range(len(B)):
    for j in range (len(B[0])):
        B[i][j]=randint(1,4)
print("Le tableau B est :", B)
print(len(B[0]))
print(len(B))


print("Voici la mult des matrices A(3,2)et B(2,4)", mult_matrice(A,B))