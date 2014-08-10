#!/usr/bin/python

class CoreCommand(object):
    def __init(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError
