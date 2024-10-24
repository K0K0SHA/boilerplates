# Filename: os_execute_wrapper.py
# author: K0K0$H@
# Purpose: safer and better way to call os.system()
# surrounds os.system() call with a try-catch for more safety
# returns the same return code as os.system() does, but warns if the return is != 0
# adds a little verbosity to the execution as well, improving debugging capability
# cross-platform compatible (Linux, Mac, Windows, Android)
# limitations are the same as system() in C
# more info on os.system() found here:
# https://www.geeksforgeeks.org/python-os-system-method/
# version: 0.6 (prototype)
import os


def execute(cmd):
	try:
		return_code=os.system(cmd)
		if (return_code != 0):
			print("Warning, nonzero exit code!")
			# can panic and exit() here instead
		print("command: ")
		print(cmd)
		print("return code: ")
		print(return_code)
		return return_code
	except Exception as E:
		print(E)
		print("Error occured while executing command!")
		print("Command:")
		print(cmd)
		print("Returning exit code 1")
		return 1

################################################################
# HOW TO USE
# copy/paste def into your program, before any references to it. 
# Alternatively, include this file in Python.
################################################################
# FOOTNOTES
# os.system() is a primitive way to execute stuff
# It should only be used when other libs are not available.
# subprocess is a much more powerful library for running stuff
# subprocess also comes standard in Python, just import it
# subprocess can not only multitask, but manipulate I/O
################################################################
