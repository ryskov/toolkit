#/usr/bin/python

class Extension(object):
    def __init__(self, prefix):
        self._prefix = prefix

    def getPrefix(self):
        return self._prefix

    def run(self, arg):
        raise NotImplementedError

    def introduce(self):
        raise NotImplementedError
