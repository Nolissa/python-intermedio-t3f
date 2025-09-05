"""
1.
Dados dos conjuntos, A y B, escribe un programa en Python
que imprima los elementos que se encuentran en A o en B, o en ambos.
"""
# Defino mis conjuntos
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print("Elementos que están en A o en B, o en ambos:")
print(A | B)

"""
2.
Dados dos conjuntos, A y B, escribe que imprima 
los elementos que se encuentran en A y en B
"""
A = {4,5,8,9,2}
B = {5,2,6,1,3}
print("Elementos que están tanto en A como en B:")
print(A & B)

"""
3.
Dados dos conjuntos, A y B, escribe un programa que imprima el conjunto 
de los elementos que se encuentran en A o en B, pero no en ambos.
"""
A = {5,2,8,3}
B = {4,8,3,2,6}
print("Elementos que están en A o en B, pero no en ambos:")
print(A.symmetric_difference(B)) # Me retorna los valores que sean diferente entre ambos

"""
4.
Dados un conjunto, A, escribe un programa que imprima 
si el conjunto es un subconjunto de otro conjunto, B.
"""
A = {8,3,9}
B = {1,8,3,5,9,2}

print("¿A es subconjunto de B?")
print(A.issubset(B)) # True porque A es subconjunto del conjunto padre que es B

"""
5.
Dados un conjunto, A, escribe un programa que 
imprima el número de elementos del conjunto.
"""
A = {7,23,6,1,9,10} # 6
print("Número de elementos del conjunto:")
print(len(A))
