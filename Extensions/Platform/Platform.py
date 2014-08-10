#!/usr/bin/python

from Core.Extension import Extension
from Core.CoreInvoker import CoreInvoker
from Extensions.Platform.Command.PrintStringCommand import PrintStringCommand

class Platform(Extension):

    _actionMap = {
        "config": "configHandler"
    }

    def __init__(self):
        super(Platform, self).__init__('Toolkit->')

    def handleInput(self, arg):
        if not arg:
            return

        args = arg.split(' ', 1)

        command = args[0].lower()

        if len(args) > 1:
            args = args[1].split(' ')
        else:
            args = None

        action = self.translateCommand(command)

        if action != False:
            action_ = getattr(self, action)

        action_(args)

    def translateCommand(self, command):
        if command in self._actionMap:
            return self._actionMap[command]
        else:
            return "showHelp"

    def introduce(self):
        CoreInvoker.execute(PrintStringCommand('Welcome to Toolkit! A python-based tool-development platform\n\n'))

    def loadConfiguration(self, config):
        self._prefix = config['prefix']

    def configHandler(self, args):
        print(args)

    def showHelp(self, args):
        print("-- Help --\n#        #\n#        #\n#        #\n#        #\n#        #\n#        #\n#        #\n----------")




