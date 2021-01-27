# -*- coding: UTF-8 -*-

print('******* Números Inteiros Invertidos *******')

numeros_lista = []

for i in range(0, 15):
    numeros_lista.append(int(input(f"Informe o número inteiro {i + 1}/15: ")))

print(f"Os números informados em ordem inversa são {(numeros_lista[::-1])}!")