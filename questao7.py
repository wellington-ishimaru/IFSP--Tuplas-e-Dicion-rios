#-*- coding: UTF-8 -*-

print('******* Números Inteiros *******')

numeros_lista = []

for i in range(0,5):
  numeros_lista.append(int(input(f"Informe o número inteiro {i+1}/5: ")))

print(f"Os números informados foram {numeros_lista}!")