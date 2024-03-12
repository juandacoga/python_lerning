

def user_information(nombre, edad, estatura_m, estatura_cm, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")


def update_user_information():
    user_information = dict()
    nombre = input("Para empezar, dime como te llamas. ")
    user_information['nombre'] = nombre
    print()
    print("Hola ", nombre, ", bienvenido a Mi Red")
    print()

    # CÃ¡lculo de edad
    agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
    edad = 2024-agno-1
    user_information['edad'] = edad
    print()

    # CÃ¡lculo de estatura
    estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    user_information['estatura_m'] = estatura_m
    user_information['estatura_cm'] = estatura_cm

    # Cantidad de amigos
    num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
    user_information['num_amigos'] = num_amigos
    return user_information