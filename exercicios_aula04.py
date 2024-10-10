import os
os.system('cls')


# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
print('Exercicio 1:\n')

informacoes_pessoa = [
    {'nome':'Bruno',
    'idade':33,
    'cidade':'São José do Rio Preto'},
    {'nome':'Alice',
    'idade':25,
    'cidade':'Potirendaba'}
    ]
for informacao_pessoa in informacoes_pessoa:
    print(f'nome: {informacao_pessoa['nome']}, idade: {informacao_pessoa['idade']}, cidade: {informacao_pessoa['cidade']}')


# 2 - Utilizando o dicionário criado no item 1:

# 2.1 - Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
print('\nExercicio 2.1:\n')

#EXEMPLO NORMAL:
# for informacao_pessoa in informacoes_pessoa:
#     if informacao_pessoa['nome'] == 'Alice':
#         informacao_pessoa['idade'] = 55

#EXEMPLO COM OPERADOR TERNARIO:
#Comando em varias linhas - Separação logica
# informacoes_pessoa = [
#     {**pessoa, 'idade': 55} #'**' desempacota o dicionario criado pelo For abaixo e substitui a idade para 55
#     if pessoa['nome'] == 'Alice' else pessoa # aqui o if é utilizado para fazer com que a substituição só aconteça com a Alice
#     for pessoa in informacoes_pessoa
# ]

#Comando em 1 linha
informacoes_pessoa = [{**pessoa, 'idade': 55} if pessoa['nome'] == 'Alice' else pessoa for pessoa in informacoes_pessoa]
print(informacoes_pessoa)


# 2.2 - Adicione um campo de profissão para essa pessoa;
print('\nExercicio 2.2:\n')
# for informacao_pessoa in informacoes_pessoa:
#     informacao_pessoa['profissao'] = 'Desconhecida'

# o dicionario '**informacao_pessoa' criado pelo For com base no dicionario 'informacoes_pessoa' é acrescido da da informação da profissão, em seguida o valor do dicionario 'informacoes_pessoa' (antigo, sem a profissão) é substituido pelo valor do dicionario 'informacao_pessoa'.
informacoes_pessoa = [{**informacao_pessoa, 'profissao':'desconhecido'} for informacao_pessoa in informacoes_pessoa]
print(informacoes_pessoa)


# 2.3 - Remova um item do dicionário.
print('\nExercicio 2.3:\n')

#'informacao_pessoa' recebe uma nova lista que será feita através do For, mas só entrarão os registros que não tiverem o nome Alice, em seguida o valor do dicionario 'informacoes_pessoa' (antigo, com o registro da Alice) é substituido pelo valor do dicionario 'informacao_pessoa'.
informacoes_pessoa = [informacao_pessoa for informacao_pessoa in informacoes_pessoa if informacao_pessoa['nome'] != 'Alice']
print(informacoes_pessoa)


# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
print('\nExercicio 3:\n')
#'x : x**2' onde 'x' é o numero que será gerado pelo for e 'x**2' é o mesmo número elevado ao quadrado, ambos representados pela variavel 'x', em seguida os valores gerados são guardados na variavel 'numeros_quadrados'
numeros_quadrados = [{x: x**2 for x in range(1,6)}]
print(numeros_quadrados)


# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
print('\nExercicio 4:\n')

verificar_chave_existe = False
carro_buscado = 'fusca'

carros = [
    {'nome':'fusca',
    'cor':'azul'},
    {'nome':'uno',
    'cor':'branco'},
    {'nome':'ferrari',
    'cor':'vermelha'}
]

for carro in carros:
    if carro['nome'] == carro_buscado: verificar_chave_existe = True

print(verificar_chave_existe)


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
print('\nExercicio 5:\n')

palavra_buscada = 'processo'
frase = 'O tão aguardado processo seletivo da Etec de São José do Rio Preto foi publicado no Diário Oficial, anunciando a formação de cadastro reserva para docentes qualificados. Essa é uma oportunidade excelente para profissionais de nível superior que buscam atuação na Escola Técnica Estadual Philadelpho Gouvea Netto, no interior de São Paulo. Regido pela Consolidação das Leis do Trabalho (CLT) e legislação complementar, o certame possui validade de um ano, podendo ser prorrogado uma vez pelo mesmo período. Esse tipo de processo seletivo visa garantir a escolha dos melhores profissionais para a educação técnica e de ensino médio da rede Etec.'

contar_frequencia_palavra = 0
palavras_frase = frase.split(' ')
#print(palavras_frase)

for palavra_frase in palavras_frase:
    if palavra_frase == palavra_buscada: 
        contar_frequencia_palavra = contar_frequencia_palavra + 1

print(f'A palavra {palavra_buscada} apareceu {contar_frequencia_palavra} vezes na frase')