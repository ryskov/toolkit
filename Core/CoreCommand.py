#!/usr/bin/python

class CoreCommand(object):
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError
