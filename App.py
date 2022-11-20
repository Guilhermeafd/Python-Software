'''Este será meu primeiro código em Python, o meu objetivo é desenvolver um software e ir incluindo versões sendo elas
funções adicionais, como se fosse um smartphone'''

from time import sleep
import Media
import ConversorDeMoedas
import ConversorDeTemperatura
import RadarEletronico
import ParImpar

print("Inicializando...")
#sleep(5)

print("Olá, sou seu novo smarthphone")
print("Vamos começar!")

Nome = str(input("Como devo te chamar? ")).strip()
Idade = str(input("Qual a sua idade? "))
Cidade = str(input("Qual a sua cidade? ")).strip()

print("Seja Bem Vindo(a) {}!".format(Nome.title()))

print("Posso te ajudar nas seguintes funções:")
print("1- Conversor de Moedas \n2- Media \n3- Conversor de Temperatura \n4- Radar Eletrônico \n5- Par ou Impar")
Codigo = int(input("Como posso te ajudar? "))

if Codigo == 1:
    ConversorDeMoedas.ConversorDeMoedas()

if Codigo == 2:
    Media.Media()

if Codigo == 3:
    ConversorDeTemperatura.ConversorDeTemperatura()

if Codigo == 4:
    RadarEletronico.RadarEletronico()

if Codigo == 5:
    ParImpar.ParImpar()
