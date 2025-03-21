import unidecode

unicode = unidecode
# 1° Atividade

# fisrtName = input("Informe seu primeiro nome: ");
# lastName = input("Informe seu último nome: ");

# print(f"Olá, {lastName} {fisrtName}, tudo bem?");

# 2° Atividade
# text = "As vezes no silencio da noite, eu acordo pensando em nós dois.";
# print(text[::-1]);


# Palindromo
word = input("Informe uma palavra para verificarmos se ela é um palindromo: ").strip().lower()
word = unidecode.unidecode(word)
word = "".join(word.split())

if word == word[::-1]:
    print(f"A palavra {word} é um palindromo")
else:
    print(f"A palavra {word} não é um palindromo")