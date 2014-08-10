#!/usr/bin/python

from Core.CoreLoop import CoreLoop
from Extensions.Platform.Platform import Platform

platform = Platform()

loop = CoreLoop('config.yaml')
loop.run()
