# -*- coding: UTF-8 -*-

print(f'*****Leitura Strings*****')

string01 = input('Informe a primeira string: ')
string02 = input('Informe a segunda string: ')

if string01.__eq__(string02):
    print(f'\nO conteúdo e o comprimento da string1 {string01} e string2 {string02} são iguais!')

elif len(string01) == len(string02):
    print(f'\nO comprimento da string1 {string01} e string2 {string02} é igual, mas os conteudos são diferentes!')

else:
    print(f'\nOs conteudos e os tamanhos das string1 {string01} e string2 {string02} são diferentes!')