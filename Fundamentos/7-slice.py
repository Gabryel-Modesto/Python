movieName = "50 tons"

# String[inicio:fim] - indice começa no 0 | Indice final -1

# 1 - Buscar toda String a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última posição
# Sempre colocar um número a mais, pq ele sempre vai pegar o número final -1
# Ou seja, se tiver 6 caracteres, coloque 7
print(movieName[:7])

# 3 -  Bucar toda String da tarceira até a última posição
print(movieName[3:7])

"""
String[inicio:fim:passo]
 Índice começa no 0 | Indice final -1
 Passo - Determina o incremento. Por padrão esse número é o 1
"""

# 4 - Buscar tota string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos índices ímpares
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente
print(movieName[::-1])