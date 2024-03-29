# filename: miscX.py
# file purpose: Python class with misc. functionality
# not related to misc stock Python lib. 
# features safer, improved convenience scripts
# this lib is used & written by K0K0SHA's GitHub code
# TODO: replace each tab with 4 spaces
# IMPORTS AND JUSTIFICATIONS:
######################################################
import os	# for terminal execution and file ops
import platform # for OS identification
import shutil   # for checking installation

# GENERAL-PURPOSE LIB CLASS CONSIDERATIONS
#####
# add more basic functions first, and more complex ones after

# This lib does not quit or exit the program.
# Coding exits is left up to the user of the lib.

# miscX is customized to K0K0$HA's development style. 
# System intended is Linux Mint ~20

# Testing this code by importing miscX in a Python Shell causes AttributeError

class miscX:

	# class variable declaration area
	verbosity = True # verbose output for verbosity() and verbose_echo()

	def __init__(self):
		print("miscX default constructor!")
		verbosity = True

	# checks if the user is root using os.geteuid()
	def checkroot():
		if(os.geteuid() != 0):
			print("Warning, you are not root! Script may misbehave.")
			return false
		else:
			print("root verified!")
			return true

	# executes a command verbosely (shows command)
	def verbosity(cmd):
		if(self.verbosity):
			print("Executing verbose:\n")
			print(cmd)
			returncode = safe_execute(commandstr)
			return returncode
		else:
			return -1 # verbosity disabled, stay mute 


	# different verbosity adaptation, echoes str if self.verbose, and returns 0 or 1
	def verbose_echo(str):
		try:
			if ((str!=None) and (self.verbosity == True)):
				print(str)
				return 0
			else:
				return 1
		except Exception as E:
			print("ERROR")
			print(E)
			return 1

	# shuts your system down within a minute
	def shutdown():
		verbosity("shutdown")
		return -1 # unreachable

	# combines os.system() with Python's exception
	# emulates a terminal command
	def safe_execute(commandstr):
		try:
			cmd = commandstr
			exitcode = os.system(cmd)
			return exitcode
		except Exception as E:
			print("ERROR IN safe_execute(commandstr)\n")
			print(E)
			return 1


	# function name: get_input()
	# safe(r) way to get input from user
	# allows no input
	def get_input(prompt):
		try:
			if prompt == None:
				prompt = "AWAITING USER INPUT, INPUT A STRING!\n"
				verbose_echo("Default prompt in get_input()")
			inp = input(prompt)
			return inp
		except Exception as E:
			print(E)
			return None

	# modification of get_input() which ensures a user inputs something and not nothing
	# disallows no input
	def get_input_forceloop(prompt):
		try:
			if(prompt==None):
				prompt = "AWAITING USER INPUT, INPUT A STRING!\n"
				verbose_echo("Default prompt in get_input_forceloop()")
			inp = None
			while (inp == None):
				inp = input(prompt)
			return inp # shouldn't return None ever
		except Exception as E:
			print(E)
			return None


	# asks user to confirm with y/n, case insensitive using casefold()
	def user_confirm(prompt):
		try:
			i = get_input("PLEASE CONFIRM (Y/N)\n")
			run = True # classic n00b infinite runLoop
			while (run):
				if (i.casefold()=='y'):
					verbose_echo("CONFIRMED!")
					return True
				elif (i.casefold()=='n'):
					verbose_echo("DENIED!")
					return False
		except Exception as E:
			print("ERROR in user_confirm(), returning False!\n")
			print(E)
			return False


	# function name: check_install()
	# Boolean that checks if a program is installed
	# To return the directory of the Python exe, run get_install_dir()
	def check_install(program):
		try:
			if (program==None):
				print("Internal ERROR, no argument supplied to check_install. Returning False\n")
				return False
			else:
				if (shutil.which(program)!=None):
					verbose_echo("Program Found:")
					verbose_echo(program)
					return True
				else:
					print("Dependency not found:\n")
					print(program)
					yn = user_confirm("attempt manual install?")
						if (yn == True):
							a = attempt_install(program)
								if (a!="install failed"):
									return True
					return False
				return False
		except Exception as E:
			print("ERROR")
			print(E)
			return False

	def get_install_dir(program):
		try:
			return(shutil.which(program))	   # check shutil documentation, returns None if no program
		except Exception as E:
			print("ERROR\n")
			print(E)
			return None

	# function name: attempt_install()
	# parameters: program name to install
	# Checks if program is already installed, then attempts to install it
	def attempt_install(program):
		try:
			instdir = get_install_dir(program) # install directory (should be None)
			if (instdir!=None):
				print("Already installed!\nInstall location:")
				print(instdir)
				return("already installed")

			cmdstr="apt-get install "
			cmdstr = cmdstr + program
			return_code = verbosity(cmdstr)
			if(return_code != 0):
				print("install failed!\nReturn Code:\n")
				print(return_code)
				return "install failed"
		except Exception as E:
			print("ERROR")
			print(E)
			return "install failed"

	# returns 0 if already installed, or if install is successful
	def pip3_install(program):
		try:
			verbosity_echo("checking pip3 installation:")
			verbosity_echo(program)
			commandstr = "pip3 install "
			commandstr = commandstr + program
			verbosity(commandstr)
		except Exception as E:
			print("ERROR")
			print(E)
			return False
	# FILE OPERATION FUNCTIONS
	#####
	# function name: file_exists()
	# returns True if file exists in current directory, false if not
	def file_exists(filepath):
		try:
			fp = filepath
			if (os.exists(filepath)):
				verbose("File exists!")
				return True
			else:
				return False
		except Exception as E:
			print("Error")
			print(E)
			return False

	# takes a list file, returns list object
	def read_file_lines_as_list(filepath):
		try:
			fp = filepath
			if (file_exists(fp) == False):
				print("error, file does not exist:")
				print(fp)
				return None # error condition
			myfile = open(filepath, 'rw')
			Lines = myfile.readlines()
			return Lines
		except Exception as E:
			print(E)
			return None # error condition

	# allows a user to select from a list of files using a fancy TUI
	def select_from_list(list):
		try:
			if (list == None):
				return None # error condition
			l = list[0]
			# UNDER CONSTRUCTION

		except Exception as E:
			print("ERROR")
			print(E)
			#exit()
			return None # error condition

	# OS EXCLUSION FUNCTIONS
	# Guardrail functions to prevent accidental OS destruction. Allows coder to choose target OS.

	# FUNCTION NAME: exclude_windows()
	# makes sure program is not running on Windows
	# This function is mostly for the safety of Windows users.
	# related to get_os_details()
	def exclude_windows():
		if (platform.system() == 'Windows'):
			print("Cannot run this script on Windows!")
			#exit()
			return False
		else:
			print("Suitable Environment detected. Proceeding...")
			return True
			#exit()

	# FUNCTION NAME: linux_only()
	# a close cousin of the exclude_windows() function
	# only allows execution on a Linux-type environment, when you want to be as exclusive as possible.
	# this function should filter users of Mac, Windows, iOS, and anything which isn't using the Linux kernel.
	def linux_only():
		if(platform.system() == 'Linux'):
			print("Linux-Like environment found!")
			return True 
		else:
			print("Linux-like environment not found!")
			#exit()
			return False



	# uses hwinfo for info (other options are ifconfig, iwconfig, and airmon-ng)
	# refer to http://www.linuxintro.org/wiki/Hwinfo
	#
	# sample hwinfo --netcard --short output:
	# 
	#network:                                                        
	#wlp5s0mon            Intel Dual Band Wireless-AC 8265
	#enp4s0               Realtek RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
	#wlx00c69420          MediaTek Wireless
	
	# Notice the first line in the output above; the one starting with network:
	# The first line should be removed when hwinfo output gets piped
	# This is automated in the get_NIC_list() function
	
	def rename_NIC(old, new):
		if !checkroot():
			return false# under construction
	
	def get_NIC_list():
		try:
			checkroot()
			if (linux_only() == False):
				print("Error, suitable environment is not found. Run on Linux!")
				return -1 # hwinfo probably doesn't work on Windows
			if (!check_install(hwinfo)):
				print("getNIC() error: hwinfo not installed")
				return -1
			commandstr = "hwinfo --netcard --short > ./.netcard.info && sed -i '1d' ./.netcard.info" # removes garbage first line
			returncode = verbosity(commandstr)
			return returncode
		except Exception as E:
			print("ERROR in get_NIC_list()")
			print(E)
			return -1

	def user_select_NIC():
		try:
			nics = get_NIC_list()
			selected_NIC = select_from_list(nics)
			return selected_NIC # should return the name of the selected network interface card
		except Exception as E:
			print("Error in user_select_NIC()")
			print(E)
			return None # error condition
			
	def show_network_drivers():
		try:
			commandstr='hwinfo --netcard | grep -Ei "model\:|driver\:'
			returncode = verbosity(commandstr)
			return returncode
		except Exception as E:
			print("Error in show_network_drivers()")
			print(E)
			return -1
	def amon():
		if !checkroot():
			print("root required for amon!")
			#exit()
			return -1
		nic = user_select_NIC()
	
		if nic:
			rename_nic(nic, "amon") # todo: MAC randomizer toggle
		else:
			return -1

