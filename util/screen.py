import os
def showHeader():
    print("============================================================")
    print("                       Bem vindo!                           ")
    print("============================================================")

    name = input("Por favor, diga-nos seu nome: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return name

def cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
