# Desafio operadores logicos

'''
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confimado: Fica em casa
'''

#Os trabalhos
trabalho_terca = True
trabalho_quinta = False

#meu jeito, interpretei o exercicio errado
if trabalho_terca and trabalho_quinta == True:
    print("Irei ao shopping comprar uma TV 50' e tomar um sorvete")
elif trabalho_terca and trabalho_quinta == False:
    print("Irei ao shopping comprar um TV 32' e tomar um sorvete")
else:
    print("Não irei ao shopping, nem tomarei sorvete, ficarei em casa")

#jeito do professor
tv_50 = trabalho_terca and trabalho_terca
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #xor
mais_saudavel = not sorvete

print("Tv50= {} Tv32= {} Sorvete {} Saudavel{}" .format(tv_50, tv_32, sorvete, mais_saudavel))
