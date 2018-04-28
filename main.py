import os
from aes.decrypt import Decrypt
from aes.encrypt import Encrypt
from util.mode import Mode
from util.params import Param


def showHeader():
    print("============================================================")
    print("                       Bem vindo!                           ")
    print("============================================================")

    result: str = input("Por favor, diga-nos seu nome: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("============================================================")
    print("               Seja bem-vindo {}".format(result))
    print("============================================================\n")

    return result


def cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def encrypt(mode: Mode):
    proccess = Encrypt(Param(mode))


def decrypt(mode: Mode):
    proccess = Decrypt(Param(mode))


name = showHeader()
response = 'a'

while response != 'x':
    print("Informe 'D' => Decriptografar")
    print("Informe 'C' => Criptografar")
    print("Informe 'X' => Sair")
    response = input()

    if response == 'c' or response == 'C':
        print('Criptografar')
        input()
        encrypt(Mode.ENCRYPT)
        cleanScreen()

    elif response == 'd' or response == 'D':
        print('Você selecionou Decriptografar')
        input('Pressione qualquer tecla para continuar... ')
        decrypt(Mode.DECRYPT)
        cleanScreen()

    elif response != 'x' or response == 'X':
        print('Opção inválida')

else:
    cleanScreen()
    print("Tchaaaaaau {}".format(name))
