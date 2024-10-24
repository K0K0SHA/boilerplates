# file name: Terminal_Output.py
# author: K0K0$H@
# purpose: demonstrate terminal I/O handling using subprocess in Python to search through output of 'ls'
# Version: 1.0
# VERSION HISTORY
# v1   10/23/2024
import os
import subprocess

cmd = "ls"

command_result = subprocess.run(cmd, capture_output=True, text=True)
command_stdout = command_result.stdout

print(command_stdout) # debug/verbosity

search_term_A = "A"
search_term_Z = "Zoroaster"

index = command_stdout.index(search_term_A)
print(f"Substring 'A' found at index {index}.")

Zcount = command_stdout.count(search_term_Z)
print(f"Substring 'Zoroaster' found {Zcount} times.")

# FOOTNOTES
# More intricate searching can be done once the output is in string form
# Sometimes, it can be more convenient to split a string by newlines or whitespaces, like in the case of wanting to search a string line-by-line
