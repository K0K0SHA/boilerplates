#!/usr/env/bin
# uses hash command to check for required dependencies, and apt to install them (need sudo for install)
# Created for Debian/Ubuntu based distros such as Mint and Kali
# This specific example of the script features several components. It is intended for the user to select their NIC easily.
# downloaded and modified from:
# https://www.linuxquestions.org/questions/programming-9/bash-function-to-check-if-script-dependencies-are-installed-4175572568/
###################################################################################################################################

if [ "$EUID" -ne 0 ]
  then
  echo "You are running this script without root. On most systems, you may not install using apt-get install without root."
  echo "This script will be able to check installed dependencies, but will probably not be able to install them for you."
  echo "If you do not wish to give this script root, then be sure to apt-get install the dependencies yourself.\n"
  # exit
fi

checkScriptDependencies () { # "${dependencies[@]}"
	local _packages=( "$@" )
	local _package=
	not_installed_pkg_count=0
	for _package in ${_packages[@]}; do
		hash $_package
		if (( $? > 0 )); then
			# sudo apt-get -y install $_package
			echo "The following package isn't installed:"
			echo $_package

			# ask user confirmation Y or y
			# check https://stackoverflow.com/questions/1885525/how-do-i-prompt-a-user-for-confirmation-in-bash-script
			read -p "Would you like to install it now using sudo apt-get install? " -n 1 -r
			echo    # newline
			if [[ $REPLY =~ ^[Yy]$ ]]
				then
				# user confirmed yes, now do stuff
				sudo apt-get -y install $_package
				else
				not_installed_pkg_count++
			fi
		fi
	done
} # end checkScriptDependencies

dependencies=('ifconfig' 'airmon-ng' 'zenity' 'grep' 'python3' 'pip3' 'iwconfig')
checkScriptDependencies "${dependencies[@]}"

if((not_installed_pkg_count > 0)); then
	echo "Packages required, but not installed (count):"
	echo not_installed_pkg_count
fi

