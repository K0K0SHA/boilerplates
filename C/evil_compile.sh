#!/bin/bash
# filename: evil_compile.sh
# purpose: compiles ./evil_code.c into ./Chrome_Setup.exe
gcc "./evil_code.c" -o "./Chrome_Setup.exe"

# notes:
# payloads go in evil_code.c
# hash comparison will detect this isn't an actual Chrome installer
