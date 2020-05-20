#-----------------------------------------------EXERCICIO 11 - TUPLAS -----------------------------------------------------------------------------------------------------------------------------------------------------------

#Tupla vazia, a partir da chamada da classe tupla
tupla = tuple()

tupla = ()
print(type(tupla))
#>> <class 'tuple>


print(dir(tupla))
#>> ['count', 'index']

# dessa maneira, apenas adiciona a string um, a variavel tupla
tupla = ('um')

tupla = ('um',)
print(tupla)
#>> ('um',)

#indexação igual a lista
print(tupla[0])
#>> 'um'

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
# 'verde'

print(cores[-1])
#>> 'branco'

print(cores[1:])
#>>('amarelo', 'azul', 'branco')

#-----------------------------------------------FIM DO EXERCICIO 11 - TUPLAS-----------------------------------------------------------------------------------------------------------------------------------------------------------


