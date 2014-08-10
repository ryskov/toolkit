#!/usr/bin/python

from Core.CoreLoop import CoreLoop

loop = CoreLoop.createLoop('config.yaml')
loop.run()
