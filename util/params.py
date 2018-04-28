from typing import TextIO
from util.mode import Mode


class Param:
    sizeKey: int
    key: str = ''
    file: TextIO
    pathFile: str = ''

    operationMode: Mode = Mode.UNDEFINED

    def __init__(self, mode: Mode):
        self.operationMode = mode

        print("Já vamos começar! Mas primeiro precisamos de algumas informações: ")
        while self.operationMode is Mode.UNDEFINED:
            print("Por gentileza informe o tipo de operação:")
            aux = input("'C' => Cripografar\n'D' => Decriptografar")
            self.operationMode = Mode.ENCRYPT if aux is 'C' else Mode.DECRYPT if aux is 'D' else Mode.UNDEFINED

        while self.pathFile == '':
            try:
                self.pathFile = input("Informe o caminho do arquivo a ser processado: ")
                self.file = open(self.pathFile, 'r')
                self.file.close()
            except IOError:
                print("Arquivo não encontrado!")
                self.pathFile = ''

        self.key = input("Infome a chave (8 ou 16 caracteres): ")
        self.sizeKey = len(self.key)

        while self.sizeKey != 8 and self.sizeKey != 16:
            self.key = input("Infome a chave (8 ou 16 caracteres): ")
            self.sizeKey = len(self.key)

