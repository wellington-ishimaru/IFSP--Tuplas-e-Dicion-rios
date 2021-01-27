# -*- coding: UTF-8 -*-
print('******* Conta Consoante *******\n')

consoante = 'bcdfghjklmnpqrstvwxyz'.upper()
lista_consoante = list(consoante)
lista_lida = []
conta_consoante = 0
consoantes_lidas = []

for i in range(0, 10):
    lista_lida.append(input(f"Digite {i + 1}/10 caracteres: "))

for char in lista_lida:
    if lista_consoante.__contains__(char.upper()):
        conta_consoante += 1
        consoantes_lidas.append(char)

print(f'\nForam lidas {conta_consoante} consoante(s) e \n '
      f'as consoantes foram: \n {consoantes_lidas}')