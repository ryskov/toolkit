#!/usr/bin/python

class Switch(object):
	"""The INVOKER class"""
	@classmethod
	def execute(cls, command):
		command.execute()

class Command(object):
	"""The COMMAND interface"""
	def __init__(self, obj):
		self._obj = obj

	def execute(self):
		raise NotImplemented

class TurnOnCommand(Command):
	"""The COMMAND for turning on the light"""
	def execute(self):
		if self._obj.get_state() == 'OFF':
			self._obj.turn_on()
		else:
			Switch.execute(PrintErrorCommand(self._obj))

class TurnOffCommand(Command):
	"""The COMMAND for turning off the light"""
	def execute(self):
		if self._obj.get_state() == 'ON':
			self._obj.turn_off()
		else:
			Switch.execute(PrintErrorCommand(self._obj))

class PrintErrorCommand(Command):
	"""The COMMAND for printing the error message"""
	def execute(self):
		print('ERROR: ' + self._obj.get_error())

class Light(object):
	"""The RECEIVER class"""

	def __init__(self):
		self._state = 'OFF'

	def turn_on(self):
		print("The light is on")
		self._state = 'ON'

	def turn_off(self):
		print("The light is off")
		self._state = 'OFF'

	def get_state(self):
		return self._state

	def get_error(self):
		return 'Already in state ' + self._state

class LightSwitchClient(object):
	"""The CLIENT class"""
	def __init__(self):
		self._lamp = Light()
		self._switch = Switch()

	def switch(self, cmd):
		cmd = cmd.strip().upper()
		if cmd == "ON":
			Switch.execute(TurnOnCommand(self._lamp))
		elif cmd == "OFF":
			Switch.execute(TurnOffCommand(self._lamp))
		else:
			print("Argument 'ON' or 'OFF' is required.")



