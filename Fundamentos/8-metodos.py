#Case sensitive
movieName = "Velozes e Furiosos"

movieDescripition = """
    Velozes e Furiosos, é uma saga de filmes que tem por 
    virtude carros, velocidade e roubos.
"""

print(movieName.upper())
print(movieName.lower())

# Deixar so a primeira letra em maiúscula
print(movieName.capitalize())

# Deixar as Primeiras letras em maiúscula
print(movieName.title())

# Retorna a string centralizada com o Caractere de preenchimento
print(movieName.center(20, '-')) 


# Retorna o indice de um determinado caractere
print(movieName.find("s"))

# Conta caracteres
print(movieName.find("s"))

# Altera um elemento por outro
print(movieName.replace("Velozes e", "Fogo"))

print(movieDescripition.split(','))





