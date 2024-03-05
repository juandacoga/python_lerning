import pyshorteners

# URL a acortar
url = "https://www.ejemplo.com/algo/muy/largo"

# Crear un objeto Shortener
shortener = pyshorteners.Shortener()

# Acortar la URL
short_url = shortener.tinyurl.short(url)

# Imprimir la URL acortada
print("URL acortada:", short_url)
