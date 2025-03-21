#Case sensitive
movieName = "Velozes e Furiosos"
movieName2 = "velozes e Furiosos"
print(movieName == movieName2)


# Strings multilinhas
movieDescripition = """
    Velozes e Furiosos, é uma saga de filmes que tem por 
    virtude carros, velocidade e roubos.
"""
print(movieName)

# Multiplicação de Strings
line = "="
print(line*60)
print(movieDescripition)

# Procurandr uma palavra dentro de um texto
print("Velozes" in movieName)
print("ação" in movieName)