#!/usr/bin/python

from Core.CoreCommand import CoreCommand

class CoreInvoker(object):
    """The CORE Invoker class"""
    @classmethod
    def execute(cls, command):
        if isinstance(command, CoreCommand):
            command.execute()
        else:
            raise AttributeError
