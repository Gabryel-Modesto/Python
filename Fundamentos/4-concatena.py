# contatenação de valores

name = input("Digite o nome do filme: ");
yearLaunch = int(input("Digite seu ano de lançamento: "));
noteMovie = float(input("Digite a nota do filme para você: "));


# Alternativa 1
print("Dados do Filme")
print("=================================")
# print("Nome do filme:", name);
# print("Ano de lançamento: ", yearLaunch);
# print("Nota do filme:", noteMovie);
# print("===================================")

# # Alternativa 2
# print("Nome do filme:", name, "\nAno de lançamento: ", yearLaunch, "\nNota do filme:", noteMovie )

# Alternativa 3
print(f"Nome do filme: {name} \n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}"
      )