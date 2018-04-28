from util.params import Param


class Decrypt:
    param: Param

    def __init__(self, params: Param):
        self.param = params

    def start(self):
        self.includeKey()
        self.__proccess()

    def includeKey(self):
        pass

    def __proccess(self):
        pass


    def openFile(self):
        pass