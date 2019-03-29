#!/usr/bin/bash

import datetime

class directory:
	def __init__(self, name, parent):
		self.name = name;
		self.parent = parent;
		self.children = []
		self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")



	def getPath(self):
		path = self.name + "/";
		while(self.parent != None):
			path = self.parent.name + "/" + path
			self = self.parent

		path += "$ "

		return path


	def processCommand(self, command):

		if command[0] == "cd":
			return self.cd(command)

		elif command[0] == "mkdir":
			self.mkdir(command)


		elif command[0] == "ls":
			self.ls(command)

		elif command[0] == "mv":
			self.mv(command)

		return 0


	def mkdir(self, command):
		#print("MKDIR")
		if len(command) == 1:
			print("mkdir error: No arguments given")
			return

		for i in range(len(self.children)):
			if command[1] == self.children[i].name:
				print("Directory of that name already exists.")
				return

		newDir = directory(command[1], self)
		self.children.append(newDir)

	def ls(self, command):
		#print("LS")
		if len(command) > 1:
			if command[1] == "-l":
				for i in range(len(self.children)):
					print(self.children[i].date + " " + self.children[i].name)
			else:
				print("ls error: Unrecognized argument")

		else:
			content = ""
			for i in range(len(self.children)):
				content = content + self.children[i].name + '\t'

			print(content)

		

	def cd(self, command):
		#print("CD")

		if len(command) == 1: # blank cd
			while(self.parent != None):
				self = self.parent
			return self

		if (command[1] == "..") and (self.parent != None): # cd to parent
			return self.parent

		for i in range(len(self.children)): # cd to child
			if command[1] == self.children[i].name:
				return self.children[i]

		path = command[1].split("/") # cd to filepath

		for i in range(len(path)):
			if path[i] == "..":
				if self.parent != None:
					self = self.parent
					continue
				else: 
					print("Invalid path")
					return 0
			else:
				for j in range(len(self.children)): 
					if path[i] == self.children[j].name:
						self = self.children[j]
						break
					elif j == (len(self.children) - 1):
						print("Invalid path")
						return 0

		return self


	def mv(self, command):

		if len(command) != 3: # incorrect number of args
			print("mv error: Incorrect number of arguments.")
			return

		for i in range(len(self.children)):
			if command[1] == self.children[i].name:
				break
			elif i == (len(self.children) - 1): # name not found
				print("mv error: source file not found")
				return

		for j in range(len(self.children)): 
			if command[2] == self.children[j].name: # move into another directory
				self.children[j].children.append(self.children[i])
				self.children[i].parent = self.children[j]
				for k in range(len(self.children)):
					if self.children[k].name == self.children[i].name:
						self.children.pop(k)
						return
			elif j == (len(self.children) - 1):
				self.children[i].name = command[2]
				break












