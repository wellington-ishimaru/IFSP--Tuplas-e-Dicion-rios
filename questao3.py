#-*- coding: UTF-8 -*-
print('Digite seu CPF no seguinte formato. \n')
cpf = list((input('XXX.XXX.XXX-XX: ')))
cpfLimpo = []
for digito in cpf:
  if digito != '.' and digito != '-':
    cpfLimpo.append(digito)

multiplicador = 10
somaValidador = 0
for i in range(0,9):
    validador1 = int(cpfLimpo[i]) * multiplicador
    somaValidador += validador1
    multiplicador -= 1
digitoValidador1 = (somaValidador * 10) % 11

multiplicador2 = 11
somaValidador2 = 0
for i in range(0,10):
    validador2 = int(cpfLimpo[i]) * multiplicador2
    somaValidador2 += validador2
    multiplicador2 -= 1

digitoValidador1 = (somaValidador * 10) % 11
digitoValidador2 =  (somaValidador2 * 10) % 11

if digitoValidador1 == 10:
  digitoValidador1 = 0
if digitoValidador2 == 10:
  digitoValidador2 = 0

print()
if digitoValidador1 == int(cpfLimpo[9]) and digitoValidador2 == int(cpfLimpo[10]):
  print(f'O CPF é valido!')
else:
  print(f'O CPF é invalido!')