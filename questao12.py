#-*- coding: UTF-8 -*-
print('******* Leitura de Notas *******\n')
index = 0
notas = []
aluno_nota = ()
todos_alunos = []

while index < 10:
  aluno_lido = input("Digite o nome do aluno: ")
  notas.clear()
  for i in range(0, 4):
    notas.append(float(input(f"Digite a {i+1}/4 nota: ")))
  aluno_nota = (aluno_lido, notas.copy())
  todos_alunos.append(aluno_nota)
  index += 1
todos_alunos_dic = dict(todos_alunos)
conta_aluno = 0
for n in todos_alunos_dic:
  media = sum(todos_alunos_dic[n])/ len(todos_alunos_dic[n])
  if media >= 7:
    conta_aluno +=1
print(f'{conta_aluno} aluno(s) com media 7 ou maior.')