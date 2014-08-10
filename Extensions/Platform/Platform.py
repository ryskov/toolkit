#!/usr/bin/python

from Core.Extension import Extension
from Core.CoreInvoker import CoreInvoker
from Extensions.Platform.Command.PrintStringCommand import PrintStringCommand

class Platform(Extension):
    def __init__(self):
        super(Platform, self).__init__('Toolkit->')

    def run(self, arg):
        CoreInvoker.execute(PrintStringCommand('Testing: ' + arg))

    def introduce(self):
        CoreInvoker.execute(PrintStringCommand('Welcome to Toolkit! A python-based tool-development platform\n\n'))

    def loadConfiguration(self, config):
        self._prefix = config['prefix']

