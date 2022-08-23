import os
import miscX as X
# filename: compile_run_custom_executable_name.py
# file purpose: cross-platform gcc compilation
commandstr = "gcc ./evil_code.c -o Chrome_Setup.exe" # shell code. gcc -o is file output option. 
X.verbosity(commandstr)
# dependency-less unsafe alternative (uncomment next line, comment previous):
#os.system(commandstr)
