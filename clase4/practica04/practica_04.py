'''1. Haciendo uso de comprensión de listas realice un programa que, dado
una lista de listas de números enteros, devuelva el máximo de cada
lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
El programa debe devolver el mayor elemento de cada sublista
(señalado en negrita).'''

my_list_01 = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

print(list(max(i) for i in my_list_01))

'''Haga uso de la función filter para construir un programa que, dado
una lista de n números devuelva aquellos que son primos. Por
ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente
debe devolver como resultado [3, 5, 5, 13]'''

my_list_02 = [3, 4, 8, 5, 5, 22, 13]
is_prime_list =[]

def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            break
        is_prime_list.append(n)
        return is_prime_list
1
        
l1 = filter(is_prime,my_list_02)
print(list(l1))