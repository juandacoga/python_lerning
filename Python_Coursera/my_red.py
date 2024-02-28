#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuaciÃ³n preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta informaciÃ³n en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el cÃ³digo, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco mÃ¡s del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su aÃ±o de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#Â¿CÃ³mo lo haremos?, usaremos una variable para guardar el resultado del cÃ¡lculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuaciÃ³n le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta informaciÃ³n para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos serÃ¡ escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambiÃ©n estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de lÃ­nea que ocurran en el cÃ³digo se considerarÃ¡n como parte del string.
# Si no estÃ¡s convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""              _                  __
__________.__       .__              .__                      .__                
\______   \__|_____ |__| ____   ____ |  | _____  ______  __ __|  |  __ __  ______
 |     ___/  \____ \|  |/    \_/ __ \|  | \__  \ \____ \|  |  \  | |  |  \/  ___/
 |    |   |  |  |_> >  |   |  \  ___/|  |__/ __ \|  |_> >  |  /  |_|  |  /\___ \ 
 |____|   |__|   __/|__|___|  /\___  >____(____  /   __/|____/|____/____//____  >
             |__|           \/     \/          \/|__|                         \/ 

""")

#Primera interacciÃ³n. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Pipinelapulus")
print()

#Segunda interacciÃ³n. Solicitamos el ingreso del aÃ±o, y utilizamos este
#dato para estimar la edad de la persona. Â¿Por quÃ© decimos que solo estamos "estimando" su edad?
#Â¿QuÃ© ocurre si eliminamos la conversiÃ³n a tipo de dato 'int' de la siguiente lÃ­nea?
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2024-agno-1
print()

#Tercera interacciÃ³n. Solicitamos la estatura, medida en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centi­metros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
print()

sexo = int(input('Cuéntame por favor tu sexo: 1 = Máculino, 2 = Femenino, 3 = No Aplica '))
if sexo == 1:
    sexo_letra = "M"
elif sexo == 2:
    sexo_letra = "F"
else:
    sexo_letra = "N/A"
print()

telefono = str(input('Dime cuál es tu numero telefonico. '))
print()

pais = str(input('Dime cuál es el país de recidencia actual. '))
print()

ciudad = str(input('Y cuál es la ciudad de recidencia actual. '))
print()

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Sexo:    ", sexo_letra)
print("Telefono:", telefono)
print("Pais:    ", pais)
print("Ciudad:  ", ciudad)
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Pipinelapulus")
print()

input("Toca enter para continuar.")

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecuciÃ³n hasta que el usuario desee salir
while continuar:

    #Solicitamos opciÃ³n al usuario
    print("--------------------------------------------------")
    opcion = int(input("""
    MENÚ =°<°= 
                       
    Dijita el número que corresponda a la opción del menú:

    1. ¿Deseas escribir un mensaje? 
    2. Ver datos del perfil.
    3. Cambiar nombre de perfil.
    4. Salir (^'w'^)
    
    Opción: """))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if opcion == 1:
        print()
        mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
    elif opcion == 2:
        print()
        print("Muy bien,", nombre, ". Estos son los datos de tu perfil.")
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "años")
        print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
        print("Sexo:    ", sexo_letra)
        print("Telefono:", telefono)
        print("Pais:    ", pais)
        print("Ciudad:  ", ciudad)
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()
        input("Toca enter para continuar.")
    elif opcion == 3:
        print()
        nuevo_nombre = input("Ingresa tu nuevo nombre de usuario: ")
        confirmacion = str(input('Esta seguro que desea cambiar su nombre por: '+nuevo_nombre+' (escriba s para comfirmar o no se realizara el cambio)'))
        if confirmacion == 's':
            nombre = nuevo_nombre
        print()
    elif opcion == 4:
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Pipinelapulus. ¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acciÃ³n de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar mÃ¡s acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafÃ­os:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opciÃ³n al usuario.
#
#2. Modifica este menÃº para que le permita el usuario realizar mÃ¡s de una acciÃ³n.
#   Por ejemplo, puedes agregar una acciÃ³n que permita al usuario modificar su nombre.