#-*- coding: UTF-8 -*-
print('******* Numeros pares e impares *******\n')

numeros = []
pares = []
impares = []

for i in range(0, 5):
  numeros.append(int(input(f'Digite {i+1}/15 numero: ')))

for num in numeros:
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)


print(f'\nA lista de numeros e: {numeros}')
print(f'A lista de pares e: {pares}')
print(f'A lista de impares e: {impares}')