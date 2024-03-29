def funcion(n1, n2):
  mayor = 0
  menor = 0
  if (n1 == 0 and n2 == 0):
    return 0
  if (n1 == 0 or n2 == 0):
    if (n1 == 0):
      return n2
    return n1
  if (n1 == n2):
    return n1
  
  if (n1 > n2):
    mayor = n1
    menor = n2
  else:
    mayor = n2
    menor = n1

  residuo = mayor % menor

  while residuo != 0:
    mayor = menor
    menor = residuo
    residuo = mayor % menor

  return menor

def potencia_mayor(numero):
  n = 0
  resultado = 0
  while resultado <= numero:
    n += 1
    resultado = 2 ** n

  return n-1

# print(potencia_mayor(65))

def panprimo(n):
  if (n < 1023456789):
    return False
  # creamos un set con una lista que se genera automaticamente del 0 al 9
  set_number = set([i for i in range(10)])
  list_number = []
  for i in sorted(str(n)):
    list_number.append(int(i))
  set_list_number = set(list_number)
  is_pandigital = set_number.issubset(set_list_number)

  last_number = int(str(n)[-3:])
  is_prime = True
  for i in range(2, last_number):
    if last_number % i == 0:
      is_prime = False
      break

  if (is_pandigital and is_prime):
    return True
  return False

# print(panprimo(1012344885769111))
# print(panprimo(2424643))


def practica():
  s = input("Ingresa una palabra: ")
  resultado = ""
  i = 0
  while i<len(s):
    resultado= resultado + s[len(s)-i-1]
    i=i+1
  print(resultado)

practica()
def mezclador(string_a, string_b):
  a = string_a[0:2]
  b = string_b[-2:]
  # aquí debes escribir el código de tu programa
  return str(a+b) # aquí debes retornar el resultado

def intercalar(string_a, string_b):
  new_word = ""
  for i in range(0, len(string_a)):
    new_word += string_a[i] + string_b
  return new_word

def ocurrencias(string):
  unos = 0
  ceros = 0
  for i in range(0,len(string)):
    if string[i] == "1":
      unos += 1
    elif string[i] == "0":
      ceros += 1
  return unos - ceros # aquí debes retornar el resultado

def remover_enesimo(s, n):
  return s[:int(n)] + s[int(n)+1:]


def reemplazo(string):
  string = str(string)
  new_word = ''
  for i in range(0, len(string)):
    if (string[i] != ' ' and string[i] == string[i].upper()):
      new_word += "$"
    else:
      new_word += string[i]
  return new_word # aquí debes retornar el resultado

print(reemplazo("Viva la Vida"))
