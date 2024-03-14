### List Comprehension ###

# Lista del 0 al 7 creada manualmente 
my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

# Lista del 0 al 7 creada con un for y un rango 
# a i se le asigna el valor de i dentro del for en el rango que le decimos
my_list = [i for i in range(8)]
print(my_list)

# Lista del 0 al 7 creada con la función list() y una varible rango
my_range = range(8)
print(list(my_range))

# esta recorriendo cada valor del rango y una vez se los asigna a i se le suma 1
# modificando así el valor que se asigna en la lista 
my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in range(8)]
print(my_list)

# Crear una lista sin los valores de un rango en un ciclo for