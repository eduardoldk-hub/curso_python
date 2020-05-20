#-----------------------------------------------EXERCICIO 11 - INDEXAÇÃO DAS LISTAS -----------------------------------------------------------------------------------------------------------------------------------------------------------


lista = [1, 5,  'Juracy', 'Leonardo', 3.1415]
# print(help(list.index))
print(lista.index('Juracy'))
#>>2 retorna o indice do valor, ou seja a posição do valor dentro da lista, começa em 0.

# print(lista.index(42))
#>> Traceback (most recent call last):
#>>   File "c:\Users\Edu\Desktop\curso_python\notas\Exercicios Apostila python\Exerc�cio 11 - Indexa��o das Listas.py", line 6, in <module>
#>>     print(lista.index(42))
#>> ValueError: 42 is not in list

print(lista[2])
#>> 'Juracy'

print(1 in lista)
#>> True

print('Juracy' in lista)
#>> True

print('Jõao' in lista)
#>> False

print(lista[0])
#>> 1

print(lista[4])
#>> 3.1415

print(lista[-1])
#>> 3.1514

print(lista[-5])
#>>

#-----------------------------------------------FIM DO EXERCICIO 11 - INDEXAÇÃO DAS LISTAS-----------------------------------------------------------------------------------------------------------------------------------------------------------










