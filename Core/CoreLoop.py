#!/usr/bin/python

import yaml
import os
from Core.Extension import Extension

class CoreLoop(object):

    def __init__(self, configFile):
        config = yaml.load(open(os.path.dirname(__file__) + '\\..\\' + configFile, 'r'))
        coreConfig = config['core']

        startupExtension = coreConfig['startup_extension']

        startupModule = 'Extensions.' + startupExtension + '.' + startupExtension
        startupModule_ = __import__(startupModule)

        mirror_ = getattr(startupModule_, 'Platform')
        instance = mirror_()

        if isinstance(instance, Extension):
            self._current_extension = instance
        else:
            raise AttributeError

    def run(self):
        self._current_extension.introduce()
        while True:
            usrInput = input(self._current_extension.getPrefix() + ' ')
            self._current_extension.run(usrInput)
