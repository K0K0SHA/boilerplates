#!/usr/bin/bash

# checks if python is installed
check_python() {
    if hash python3 2>/dev/null; then
        echo "Python 3 installed!"
    else
        echo "Python 3 not installed! Try installing with sudo apt-get install python3 or sudo apt-get install python3-dev."
    	echo "...Attempting install!. This will only work with sudo."
	apt-get -y install python3
    fi
}

check_pip() {
    if hash pip3 2>/dev/null; then
	echo "pip3 installed!"
    else
	echo "pip3 not installed! Try installing with sudo apt-get install python3-pip, or run this script as sudo."
	apt-get -y install python3-pip
    fi
}

check_python
check_pip
