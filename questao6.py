#-*- coding: UTF-8 -*-
from random import randint

conjunto_palavras = ['banana', 'abobrinha', 'chocolate', 'cafe', 'mexerica']
jogadas = 0
while jogadas < 5:
    palavra_sorteada = list(conjunto_palavras[randint(0, len(conjunto_palavras) - 1)])
    guarda_palavra_original = "".join(palavra_sorteada)
    palavra_sorteada.sort()
    chute_usuario = input(f"Adivinhe qual e a palavra {''.join(palavra_sorteada)}: ")
    if chute_usuario == guarda_palavra_original:
        print('Parabens, voce acertou!')
    else:
        print('Que pena, voce errou!')
        print(f'Resposta correta: {guarda_palavra_original}')
    jogadas += 1
