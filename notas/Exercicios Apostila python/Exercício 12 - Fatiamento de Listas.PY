#-----------------------------------------------EXERCICIO 11 - FATIAMENTO DE LISTAS -----------------------------------------------------------------------------------------------------------------------------------------------------------


lista = [1, 5, 'Juracy', 'Leonardo', 3.1415]

print(lista[1:3])
#>> 5, 'Juracy'

print(lista[1:-1])
#>> 5, 'Juracy', Leonardo

print(lista[1:])
#>> [5, 'Juracy', 'Leonardo', 3.1415]

print(lista[:-1])
#>> [1, 5, 'Juracy', 'Leonardo']

print(lista[:])
#>> [1, 5, 'Juracy', 'Leonardo', 3.1415]

# função(variavel[posicao_inical:posicao_final:step]) -> step é o numero de vezes que será 'pulado', por default é 1
print(lista[::2])
#>>[1, 'Juracy', 3.1415]

print(lista[::-1])
#>> [3.1415, 'Leonardo', 'Juracy', 5, 1]

del lista[2]
print(lista)
#>> [1, 5, 'Leonardo', 3.1415]

del lista[1:]
print(lista)
#>> [1]

#-----------------------------------------------FIM DO EXERCICIO 12 - FATIAMENTO DE LISTAS-----------------------------------------------------------------------------------------------------------------------------------------------------------







