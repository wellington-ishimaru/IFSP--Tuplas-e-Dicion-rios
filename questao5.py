#-*- coding: UTF-8 -*-

num_telefone = list(input("Digite o numero de telefone: "))
num_corrigido = ['3']

if num_telefone.__contains__('-') and len(num_telefone) == 8:
    for digito in num_telefone:
        num_corrigido.append(digito)
    print(f'O numero de telefone e: {"".join(num_corrigido)}')
elif not num_telefone.__contains__('-') and len(num_telefone) == 7:
    for digito in num_telefone:
        num_corrigido.append(digito)
    print(f'O numero de telefone e: {"".join(num_corrigido)}')
else:
    print(f'O numero de telefone e: {"".join(num_telefone)}')

