#!/usr/bin/python

from Core.Extension import Extension

class CoreLoop(object):

    def __init__(self, firstExtension):
        if isinstance(firstExtension, Extension):
            self._current_extension = firstExtension
        else:
            raise AttributeError

    def run(self):
        self._current_extension.splash()
        while True:
            usrInput = input(self._current_extension.getPrefix() + ' ')
            self._current_extension.run(usrInput)
