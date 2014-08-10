#/usr/bin/python

class Extension(object):
    def __init__(self, prefix):
        self._prefix = prefix

    def getPrefix(self):
        return self._prefix

    def run(self, arg):
        raise NotImplsementedError

    def splash(self):
        raise NotImplementedError
