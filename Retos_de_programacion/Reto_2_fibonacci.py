number_1 = 0 
number_2 = 1
print(number_1)
for i in range(1,50):
    number_3 = number_1 + number_2
    print(number_3)
    number_2 = number_1
    number_1 = number_3

"""
Se suma y se muestra los dos primeros numeros de la secuencia 
Luego se pasa a numero 2 el valor de numero uno y numero uno se 
le asigna la suma que que se hizo anteriormente  
"""