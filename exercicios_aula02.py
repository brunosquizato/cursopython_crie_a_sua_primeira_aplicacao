import os
os.system('cls')

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
print('Exercicio 1')
numero = int(input('digite um numero: '))
resultado_divisao = numero % 2
if resultado_divisao == 0:
    print('numero par')
else:
    print('numero impar')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos; COMENTARIO: a descrição do exercicio da a entender que uma pessoa com 18 ainda é um adolescente, farei a correção
# Adulto: acima de 18 anos.
print('\n')
print('Exercicio 2')
idade = int(input('Qual a sua idade?: '))

match idade:
    case idade if idade <= 12:
        print('criança')
    case idade if 13 <= idade <= 17:
        print('adolescente')
    case idade if idade >= 18:
        print('adulto')


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
print('\n')
print('Exercicio 2')
usuario = input('Digite o seu usuario: ')
senha = input('Digite a sua senha: ')
if usuario == 'bruno' and senha == '12345':
    print('acesso ao sistema liberado')
else:
    print('acesso ao sistema bloqueado')