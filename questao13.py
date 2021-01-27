#-*- coding: UTF-8 -*-
print('******* Consumo de gasolina *******\n')
carros = []
consumo = []
preco_gasolina = 2.25
distancia_percorrida = 1000
for i in range(0, 5):
    carros.append(input('Digite o modelo do carro: '))
    consumo.append(float(input('Digite o consumo do carro km/l: ')))
for i in range (0, 5):
    qtd_l = round(1000 / consumo[i], 2)
    qtd_rs = round(1000 / consumo[i] * preco_gasolina, 2)
    print(f'{i+1} - {carros[i]} - {consumo[i]} - {qtd_l} - R${qtd_rs}')
print(f'O carro mais economico e: {carros[consumo.index(max(consumo))]}')