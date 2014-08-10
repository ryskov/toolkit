#!/usr/bin/python

import yaml
import os
from Core.Extension import Extension
from Core.Exception.CoreErrorException import CoreErrorException
from Core.Exception.ConfigurationErrorException import ConfigurationErrorException

class CoreLoop(object):

    _current_extension = None
    _extensions = {}
    _suppressCoreWarnings = False

    def __init__(self, configFile):
        config = yaml.load(open(os.path.dirname(__file__) + '\\..\\' + configFile, 'r'))

        coreConfig = config['core']

        suppressCoreWarnings = coreConfig['suppress_core_warnings']

        self._suppressCoreWarnings = suppressCoreWarnings

        extensionConfig = config['extensions']
        extensions = extensionConfig['extensions']

        for extension in extensions:
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
                raise AttributeError

            if extension.lower() in extensionConfig:
                self._extensions[extension].loadConfiguration(extensionConfig[extension.lower()])

        startupExtension = coreConfig['startup_extension']

        self._current_extension = startupExtension

    def run(self):
        self._extensions[self._current_extension].introduce()
        while True:
            usrInput = input(self._extensions[self._current_extension].getPrefix() + ' ')
            self._extensions[self._current_extension].run(usrInput)
