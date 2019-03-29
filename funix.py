#!/usr/bin/bash

import directory

class funix:
	def __init__(self, rootDirectory):
		self.currentDirectory = rootDirectory

	def run(self):
		while(True):
			command = raw_input(self.currentDirectory.getPath())
			command = command.strip()
			command = command.split(' ')
			input = self.checkInput(command)

			if input == 0:
				break;

			elif input == 1:
				#error
				print("Invalid command")
				continue

			else:
				#correct command
				newDir = self.currentDirectory.processCommand(command)
				if newDir != 0:
					self.currentDirectory = newDir
				continue


	def checkInput(self, command):
		
		#print(command)
		if (command[0] == "exit") and (len(command) == 1):
			return 0
		if (self.validCommand(command[0])):
			return 2
		else:
			return 1



	def validCommand(self, command):
		validCommands = ["cd", "mkdir", "ls", "mv", "cp", "rm"]
		if command in validCommands:
			return True
		else:
			return False




rootDirectory = directory.directory("~", None)
myFunix = funix(rootDirectory)
myFunix.run()


'''
Root
Documents Downloads Pictures
Pictures Books 
'''