#-*- coding: UTF-8 -*-

name = input('Digite seu nome completo: ').upper()
index = len(name)

#"fatiando" a string
reversed_name = name[index::-1]
print(reversed_name)

#usando loop
reversed_str = []
while index > 0:
    reversed_str += name[index - 1]
    index -= 1
print(reversed_str)

#usando metodo join()
name_inverted = ''.join(reversed(name))
print(name_inverted)