# filename: compile_C_Linux.sh
# author: K0K0$H@
# purpose:
# compiles demo.c and runs it on Linux system using gcc
# basic example script; will not check dependencies
# if you have g++, you could use that instead
# this script won't build programs which require make
#!/usr/bin/env bash

gcc demo.c && ./a.out
