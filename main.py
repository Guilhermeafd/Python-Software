'''Este será meu primeiro código em Python, o meu objetivo é desenvolver um software e ir incluindo versões sendo elas
funções adicionais, como se fosse um smartphone'''

from time import sleep

print("Inicializando...")
sleep(5)

print("Olá, sou seu novo smarthphone")
print("Vamos começar!")

Nome = str(input("Como devo te chamar? ")).strip()
#Idade = str(input("Qual a sua data de nascimento? "))
#Cidade = str(input("Qual a sua cidade? ")).strip()

print("Seja Bem Vindo(a) {}!".format(Nome.capitalize()))

print("Posso te ajudar nas seguintes funções:")
print("1- Conversor de Moedas \n2- Media \n3- Conversor de Temperatura")
Codigo = int(input("Como posso te ajudar? "))