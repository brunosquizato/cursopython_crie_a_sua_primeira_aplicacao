import os
os.system('cls')
from datetime import date


# 1 - Crie uma lista para cada informação a seguir:

# * Lista de números de 1 a 10;
# * Lista com quatro nomes;
# * Lista com o ano que você nasceu e o ano atual.

print('Exercicio 1:\n')

lista_um_a_dez = [1,2,3,4,5,6,7,8,9,10]
for lista_um_a_dez in lista_um_a_dez:
    print(lista_um_a_dez)

print()

lista_quatro_nomes = ['Bruno','Eliana','Taison','Marcelo']
for lista_quatro_nomes in lista_quatro_nomes:
    print(lista_quatro_nomes)

print()

hoje = date.today()
lista_ano_nascimento_ano_atual = [1991,hoje.year]
for lista_ano_nascimento_ano_atual in lista_ano_nascimento_ano_atual:
    print(lista_ano_nascimento_ano_atual)

print()


# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

print('\nExercicio 2:\n')

numeros_aleatorios = [1,36,50,25,68,44,33,78,87,99,150,145,250,690]
for numeros_aleatorios in numeros_aleatorios:
    print(numeros_aleatorios)


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

print('\nExercicio 3:\n')

resultado_soma_impares = 0

for i in range(1, 11):
    if i % 2 != 0:
        resultado_soma_impares = resultado_soma_impares + i
        

print(resultado_soma_impares)


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

print('\nExercicio 4:\n')

lista_do_dez_ao_zero = [10,9,8,7,6,5,4,3,2,1,0]
for lista_do_dez_ao_zero in lista_do_dez_ao_zero:
    print(lista_do_dez_ao_zero)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

print('\nExercicio 5:\n')

numero_tabuada = input('digite um número: ')
for i in range(1, 11):
    print(f'{numero_tabuada} x {i} = {int(numero_tabuada)*i}')


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

print('\nExercicio 6:\n')

resultado_soma_numeros = 0
lista_numeros = [5,10,15,20,"25",30,"a"]

for lista_numeros in lista_numeros:
    try:
        resultado_soma_numeros = resultado_soma_numeros + int(lista_numeros)
    except:
        print(f'O elemento "{lista_numeros}" da lista não é um número valido e por isso não será somado ao resultado!')

print(f'resultado da soma: {resultado_soma_numeros}')


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

print('\nExercicio 7:\n')

#lista_de_valores = [1,66,99,88,77]
lista_de_valores = []
soma_valores = 0

# em listas no For, a primeira variavel é utilizada para armazenar o valor do elemento atual no qual o For está trabalhando, quando utilizamos o For da seguinte maneira 'for lista in lista' estamos destruindo a lista enquanto a percorremos dentro do For, o ideal é sempre criar uma nova variavel para percorrer a lista sem destrui-la. Exemplo: 'for elemento_lista in lista'
for valor_da_lista in lista_de_valores:
    soma_valores = soma_valores + valor_da_lista
try:
    resultado_media_valores = soma_valores / len(lista_de_valores)
except ZeroDivisionError:
    resultado_media_valores = 0

print(resultado_media_valores)