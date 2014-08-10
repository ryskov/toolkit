#!/usr/bin/python

from Core.CoreCommand import CoreCommand

class PrintStringCommand(CoreCommand):
    def execute(self):
        print(self._obj)
