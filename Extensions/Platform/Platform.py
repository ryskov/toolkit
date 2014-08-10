#!/usr/bin/python

from Core.Extension import Extension
from Core.CoreInvoker import CoreInvoker
from Core.CoreLoop import CoreLoop
from Extensions.Platform.Command.PrintStringCommand import PrintStringCommand

class Platform(Extension):

    _actionMap = {
        "config": "configHandler",
        "clear": "clearScreen"
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

        return action_(args)

    def translateCommand(self, command):
        if command in self._actionMap:
            return self._actionMap[command]
        else:
            return "showHelp"

    def introduce(self):
        CoreInvoker.execute(PrintStringCommand('Welcome to Toolkit! A python-based tool-development platform\n\n'))

    def loadConfiguration(self, config):
        self._prefix = config['prefix']

    def clearScreen(self, args):
        import os

        clear = lambda: os.system('clear')
        clear = clear()

        if clear == 1:
            clear = lambda: os.system('cls')
            clear()

    def configHandler(self, args):
        if len(args) > 0:
            action = args[0]

            if action == 'reload':
                self.reloadConfiguration()
            elif action == 'set':
                if len(args) > 2:
                    del args[0]
                    self.setConfig(args)
            elif action == 'show':
                self.showConfig()


    def showConfig(self):
        config = open(CoreLoop._loop._config_file, 'r')
        print(config.read())

    def setConfig(self, args):
        import yaml

        config = open(CoreLoop._loop._config_file, 'r')
        configYml = yaml.load(config)
        config.close()

        fields = args[0].split('.')
        value = args[1]

        depth = len(fields)

        if depth == 1:
            configYml[fields[0]] = value
        elif depth == 2:
            configYml[fields[0]][fields[1]] = value
        elif depth == 3:
            configYml[fields[0]][fields[1]][fields[2]] = value
        elif depth == 4:
            configYml[fields[0]][fields[1]][fields[2]][fields[3]] = value
        elif depth == 5:
            configYml[fields[0]][fields[1]][fields[2]][fields[3]][fields[4]] = value

        with open(CoreLoop._loop._config_file, 'w') as outfile:
            outfile.write(yaml.dump(configYml, default_flow_style=False))

    def reloadConfiguration(self):
        CoreLoop._loop.loadConfiguration()

    def showHelp(self, args):
        print("-- Help --\n#        #\n#        #\n#        #\n#        #\n#        #\n#        #\n#        #\n----------")




