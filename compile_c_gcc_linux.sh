#!/usr/bin/env bash
# compiles demo.c and runs it on Linux system using gcc
# basic example script; will not check dependencies
# if you have g++, you should use that instead
# this will not build programs which require make
gcc demo.c && ./a.out
