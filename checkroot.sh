#!/usr/bin/bash

# basic root checker by K0K0$HA

if [ "$EUID" -ne 0 ]
  then echo "Please run this as root."
  exit
fi
