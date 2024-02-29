# primera parte del reto, definir si un numero es primo o no 

numero = 2

es_primo = True
if numero <= 1:
    es_primo = False
for i in range(2,numero):
    if numero % i == 0:
        es_primo = False
        break

print (es_primo)

#Parte dos, imprimir numeros primos del 1 al 100

for numero in range(1,101):
    es_primo = True
    if numero <= 1:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print (numero)


# mejorar código con una función 
        
def isPrime(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(isPrime(13))

for i in range(1, 101):
    if isPrime(i):
        print(i)