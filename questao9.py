#-*- coding: UTF-8 -*-
print('******* Boletim *******')
notas = []
for i in range(1, 5):
    notas.append(float(input(f"Digite a {i}a nota: ")))
media = sum(notas)/len(notas)
print(f'Notas {notas}')
print(f'Media: {round(media,2)}')
if media >= 7:
    print("Aluno aprovado!")
elif 7 > media >= 4:
    print("Aluno em exame!")
else:
    print("Aluno reprovado!")
