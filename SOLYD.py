'''RESUMO DO CURSO INTRODUTORIO AO PYTHON SOLYD
ALUNO : WADAWELL
estou iniciando, não levem isso a serio
'''

import os

# Aula 1 
aula1 = ('AULA 1 - INTRODUÇÃO AO PYTHON E CONFIGURANDO O AMBIENTE')

print (aula1)
print ('')
print ('link da aula: ')
print ('https://www.youtube.com/watch?v=uEEuSYkM9o4&list=PLp95aw034Wn_WtEmlepaDrw8FU8R5azcm')
print ('')

input ('tecle ENTER para continuar...')
os.system("cls ")
print ('........................................................')
print ('')

# Aula 2
aula2 = ('AULA 2 - Variáveis, tipos, entrada, saída e operadores matemáticos')

print ('')
print (aula2)
print ('link da aula:')
print ('')
print ('https://www.youtube.com/watch?v=jzYgWGGNh7s&list=PLp95aw034Wn_WtEmlepaDrw8FU8R5azcm&index=2')
print ('')
input ('tecle ENTER para continuar...')
os.system("cls ")

print (aula2)
print ('')
print ('                     SAIDA DE ARQUIVOS')
print ('')
print ('Confira o codigo fonte, ( / ) Esta ao contrario nos exempos abaixo: ')
print ('')


# uso do \t
print (' /t irá realizar a tabulação (6 espaços em branco) ')
input ('tecle ENTER para ver o exemplo...')
print ('')
print ('print  ("hello /t World") ')
print ('')
input ('tecle ENTER para mostrar o resultado no console...')
print ('')
print ('>>> hello\tworld')
print (' ')
print ('.........................................................')
input ('tecle ENTER para ver mais exemplos...')
os.system("cls ")

print ('')
# Exemplo de uso em criação de planilha
print (aula2)
print ('')
print (' Exemplo criação de planilia')
print ('')
print ('print ("nome /t idade /t cidade")')  
print ('print ("vinicius /t 24 /t cuiaba")')
print ('')
input ('tecle ENTER para mostrar o resultado no console...')
print ('')
print (">>>", 'nome\tidade\tcidade')
print ('')
print (">>>", 'vinicius\t24\tcuiaba')
print ('')
print ('#Lembrando que o sinal de / é invertino nos exemplos')
print ('#Use o sinal ( \ )')

print (' ')
print ('........................................................')
input ('tecle ENTER para ver sobre o /n...')
os.system("cls ")
print ('')

# uso do \n
print (aula2)
print ('')
print ('( /n ) serve para quebrar linhas, exemplo:')
print ('')
print ('print  ("hello /n World") ')
print ('')
input ('tecle ENTER para mostrar o resultado no console...')
print ('')
print ('>>> hello\nworld')
print (' ')
print ('........................................................')
input ('tecle ENTER para ver sobre as variaveis...')
os.system("cls ")
print ('')

#Variaveis
nome_exemplo = ('Vinicius')
sobrenome_exemplo = ('coelho')

print (aula2)
print ('')
print ('                       VARIAVEIS')
print ('')
print ('variaves posuem algumas caracteristicas como por exemplo , \n letras minusculas e fazer_o_uso de anderlines para concatenar palavras . ')
print ('')
print ('Armazenando valor string dentro de uma variavel')
print ('exemplo de armazenamento das variaveis nome e sobrenome:')
print (' ')
print ("nome_exemplo = 'Vinicius'" )
print ("sobrenome_exemplo = 'Coelho'")
print ("print (nome_exemplo, sobrenome_exemplo)")
print ('')
input ('tecle ENTER para mostrar o resultado no console...')
print ('')
print ('>>>', nome_exemplo, sobrenome_exemplo)
print (' ')
print ('........................................................')
input ('tecle ENTER para ver sobre a função INPUT...')
os.system("cls ")

print ('')
nome = input ('escreva seu nome: ')
sobrenome = input ('escreva seu sobrenome: ') 
print (">>> ", nome, sobrenome)
print ("#esses dados forão armazenados nas variaveis nome e sobrenome da seguinte forma")
print ('')
print ("nome = input ('escreva seu nome: ')")
print ("sobrenome = input ('escreva seu sobrenome: ')")

print ('')
input ('tecle ENTER')
os.system("cls ")

print (aula2)
print ('')
print ('Criando variavel idade com valor inteiro \n e altura com float para explicar a função type')
print ('')

idade = input ('sua idade: ')
altura = input ('sua altura: ')
os.system("cls ")

print ('')
#Função TYPE

print ('aula2')
print ('                          FUNÇÃO TYPE')
print ('                          tipo string - str')
print ('                          tipo inteiro - int')
print ('                          tipo flutuante - float')
print ('')
print ('para ver o tipo de função que cada Variavel recebe use: ')
print ('')
print ('print (type(nome))')
print ('>>>', ( type(nome)))
print ('')
print ('print (type(idade))')
print ('>>>', ( type(idade)))
print ('')
print ('print (type(altura))')
print ('>>>', (type(altura)))
print ('')
print ('........................................................')
print (' ')        
input ('ou crie uma variavel com o formato type, exemplo...')
print ('')
print ('tipo = type (nome)')
print ('tipo_idade = type (idade)')
print ('tipo_altura = type (altura)')

print ('')
input ('tecle ENTER para ver o resultado no console...')
print ('')

tipo_nome = type(nome)
tipo_idade = type (idade)
tipo_altura = type (altura)

print ('>>>', tipo_nome)
print ('>>>', tipo_idade)
print ('>>>', tipo_altura)

print ('')
print ('........................................................')
input ('tecle ENTER')
os.system("cls ")

print ('')
print ('confome vimos a variavel nome armazena uma STR/string \n por conter aspas em sua pré definição \n ja a variavel idade do tipo INT/inteiro \n por não conter aspas em sua pré definição;')
print ('ja to tipo float por conter um ponto flutuante ( . ) em sua pré definição')

print('')
input ('tecle ENTER')
print ('')

print ('        formas para concatenar frases atraves de variaveis')

print ('')
input ('tecle ENTER')
print ('')

#USANDO VIRGULA ,
print ('                      usando vigula: ')

print ('')
input ('tecle ENTER')
print ('')

print ('print (nome, sobrenome, "tem ", idade, "anos de idade e ", altura, "altura" )')
print ('')
print (">>>", nome, sobrenome, "tem ", idade, "anos de idade e ", altura, "de altura")

print ('')
print ('........................................................')
input ('tecle ENTER')
print ('')

#USANDO SINAL DE MAIS+
print ('                usando sinal de mais ( + ):')

print ('')
input ('tecle ENTER')
print ('')

print ('o sinal de mais não coloca espaço após imprimir \n e não reconhece outros valores alem de str. ')

print ('')
input ('tecle ENTER')
print ('')

print ('print (nome + sobrenome + " tem " + str(idade) + " anos de idade e " + str( de altura) + "altura" ')

print ('')
input ('Não vou imprimir os resultados para não alterar as variaveis nas explicaçoes anteriores ')
print ('')

#print (">>> " + nome + " " + sobrenome + " tem " + str(idade) + " anos de idade e " + str(altura) + " de altura" )
print ('')

print ('')
print ('........................................................')
input ('tecle ENTER')
print ('')

#Função input
print ('                  variavel interativa usando INPUT ')
print ('exemplo: ')

print ('')
input ('tecle ENTER')
print ('')

print ('cidade = input("escreva sua cidade: " )')
cidade = input('escreva sua cidade: ')


print ('')
input ('tecle ENTER')
print ('')

print ("morador de", cidade)

print ('')
print ('........................................................')
input ('tecle ENTER')
print ('')



# Aula 3
input ('tecle ENTER')
print ('')

aula3 = ('AULA 3 - Operadores lógicos e estruturas de decisões IF e ELSE')
print (aula3)

print ('')
print ('........................................................')
input ('tecle ENTER')
print ('')

#Aula 4 
aula4 = ('AULA 4 - strings & lista')
print (aula4)
