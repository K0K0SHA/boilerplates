# filename: exception_example.py
# purpose: shows how to handle an exception in Python, and also how not to
# TODO: add more exception examples
# Last update: 10/23/2024

# throw_ZeroDivisionError()
# divides by zero, causing Python to throw an exception automatically
def throw_ZeroDivisionError():
  myvar = 6/0
  return

# throw_NameError_no_import()
# attempts to use a package that doesn't exist, which causes a NameError exception
def throw_NameError_no_import():
  osname = os.name()
  return

# throw_NameError_no_variable()
# attempts to set the variable Ronald to the variable McDonald, which doesn't exist. This causes a NameError exception
def throw_NameError_no_variable():
  Ronald = McDonald
  return

print("\n\n")

try:
  throw_ZeroDivisionError()
except Exception as E:
  print(E)
  print("\n")
  
try:
  throw_NameError_no_import()
except Exception as E:
  print(E)
  print("\n")

try:
 throw_NameError_no_variable()
except NameError as NE:
  print(NE)
  print("\n")

# Exception within an exception, because Python uses Error to refer to it eg NameError, not NameException
try:
  throw_NameError_no_variable()
except NameException as NE:
  # the code stops ^^^ on the previous line because it doesn't recognize what NameException is:
  print(NE)
  print("\n")


# as the code appears, the execution stops before this line gets reached
throw_ZeroDivisionError()
throw_NameError_no_import()
throw_NameError_no_variable()
