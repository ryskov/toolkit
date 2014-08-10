#/usr/bin/python

class Extension(object):
    def __init__(self, prefix):
        self._prefix = prefix

    def getPrefix(self):
        return self._prefix

    def handleInput(self, arg):
        raise NotImplementedError

    def introduce(self):
        raise NotImplementedError

    def loadConfiguration(self, config):
        raise NotImplementedError

    def showHelp(self, args):
        print("No help page found for this extension")