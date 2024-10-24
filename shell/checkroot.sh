# filename: checkroot.sh
# author: K0K0$H@
# purpose: checks if $UID == 0 , eg whether this is being run as root
#!/usr/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run this as root."
  exit
fi
