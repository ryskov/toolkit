#!/usr/bin/python

import yaml
import os

from Core.Extension import Extension
from Core.Exception.ConfigurationErrorException import ConfigurationErrorException

class CoreLoop(object):

    _loop = None

    _config_file = None

    _current_extension = None
    _extensions = {}
    _suppressCoreWarnings = False

    def __init__(self, configFile):
        self._config_file = os.path.dirname(__file__) + '\\..\\' + configFile
        self._current_extension = self.loadConfiguration(True)

    @staticmethod
    def createLoop(configFile):
        CoreLoop._loop = CoreLoop(configFile)
        return CoreLoop._loop

    def loadConfiguration(self, loadExtensions = False):
        config = yaml.load(open(self._config_file, 'r'))

        coreConfig = config['core']

        self._suppressCoreWarnings = coreConfig['suppress_core_warnings']

        extensionConfig = config['extensions']
        extensions = extensionConfig['extensions']

        for extension in extensions:
            if loadExtensions == True:
                module = 'Extensions.' + extension + '.' + extension

                try:
                    module_ = __import__(module)
                except ImportError:
                    raise ConfigurationErrorException('Extension ' + extension + ' could not be loaded. Unable to import module [' + module + ']')

                mirror_ = getattr(module_, extension)
                instance = mirror_()

                if isinstance(instance, Extension):
                    self._extensions[extension] = instance
                else:
                    raise TypeError

            if extension.lower() in extensionConfig:
                self._extensions[extension].loadConfiguration(extensionConfig[extension.lower()])

        print('Configuration has been loaded!')
        return coreConfig['startup_extension']


    def run(self):
        self._extensions[self._current_extension].introduce()
        while True:
            usrInput = input(self._extensions[self._current_extension].getPrefix() + ' ')
            self._extensions[self._current_extension].handleInput(usrInput)
