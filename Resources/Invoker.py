#!/usr/bin/python

from CommandPattern import LightSwitchClient

client = LightSwitchClient()

while True:
    cmd = input("What is your order? ")
    client.switch(cmd)





