#-*- coding: UTF-8 -*-

frase = input("Digite uma frase: ").upper()

conta_espacos = 0
posicoes = []
for letra in frase:
    if letra == " ":
        posicoes.append(conta_espacos)
    conta_espacos += 1
print(f'Os espacos em branco sao {frase.count(" ")} e estao\n'
    f'nas seguintes posicoes {posicoes}.')
print(f'A frase contem {frase.count("a".upper())} vogal(is) "a",'
    f'{frase.count("e".upper())} vogal(is) "e",\n{frase.count("i".upper())} vogal(is) "i",'
    f' {frase.count("o".upper())} vogal(is) "o" e {frase.count("u".upper())} vogal(is) "u".')




