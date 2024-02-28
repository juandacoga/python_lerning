def isAnagrama(first_word, second_word):
    if first_word == second_word:
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())

print(isAnagrama('arroz', 'zorra'))

"""
Lo que hace sorted es que crea una lista ordenada con lo que se le pase
Si se le pasa una lista de numeros, ordenara del menor al mayor por defecto

Al pasarle una palabra hay que tener en cuenta que es una lista de caracteres
sorted crea una lista ordenada alfabeticamente con cada uno de los caracteres 
de la palabra 

y al comparar las listas y ver si son iguales, quiere decir que son anagramas
"""