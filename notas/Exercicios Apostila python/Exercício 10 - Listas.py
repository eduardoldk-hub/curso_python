#-----------------------------------------------EXERCICIO 10 - LISTAS -----------------------------------------------------------------------------------------------------------------------------------------------------------

lista = []
print(type(lista))
#>> <class 'list'>

print(dir(lista))
#>> 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(len(lista))
#>> 0

lista.append(1)
lista.append(5)
print(lista)
#>> [1, 5]


print(len(lista))
#>> 2

nova_lista = lista + ['Juracy', 'Leonardo', 3.1415]
print(nova_lista)
#>> [1, 5, 'Juracy', 'Leonardo', 3.1415]

#insert recebe dois argumentos
nova_lista.insert(0, 'Zero')
print(nova_lista)
#>> ['Zero', 1, 5, 'Juracy', 'Leonardo', 3.1415]

#remove recebe somente um argumento
nova_lista.remove(5)
print(nova_lista)
#>> ['Zero', 1, 'Juracy', 'Leonardo', 3.1415]

#-----------------------------------------------FIM DO EXERCICIO 10 - LISTAS -----------------------------------------------------------------------------------------------------------------------------------------------------------


