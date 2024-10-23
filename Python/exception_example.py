# filename: exception_example.py
# purpose: shows how to handle an exception in Python, and also how not to
# TODO: add more exception examples

# divides by zero, causing Python to throw an exception automatically
def throw_ZeroDivisionError():
  myvar = 6/0
  return

# attempts to use a package that doesn't exist, which causes a NameError exception
def throw_NameError_no_import():
  osname = os.name()
  return

# attempts to set the variable Ronald to the variable McDonald, which doesn't exist. This causes a NameError exception
def throw_NameError_no_variable():
  Ronald = McDonald
  return


throw_ZeroDivisionError()
throw_NameError_no_import()
throw_NameError_no_variable()
