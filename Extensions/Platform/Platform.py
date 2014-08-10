#!/usr/bin/python

from Core.Extension import Extension

class Platform(Extension):
    def __init__(self):
        super(Platform, self).__init__('Toolkit->')

    def run(self, arg):
        print('Testing: ' + arg)

    def splash(self):
        print("Welcome to Toolkit! A python-based tool-development platform\n\n")