# filename: command_parse_argparse.py
# author: K0K0$H@
# purpose: demonstrate how argparse can be used to parse optional command-line variables for host (string) and port (int)
########## This function in its current state can be used on anything that requires a host and a port, such as netcat. 
# Version: 1.1
# Version History
# 1.0     10/23/2024
# 1.1     10/23/2024

# sample usage 1: python3 command_parse_primitive.py --host challenge.ctf.org -p 2222
# sample usage 2: python3 command_parse.py --help
import argparse

def parse_cmdline_args():
    parser = argparse.ArgumentParser(description = "<Program Description> This is a program that allows a user to pass in a host and a port number via command-line arguments. Originally, it was made to help with CTFs (Capture the Flag Challenges) where a challenge may require a host and a port to connect. In order to maintain simplicity, this file merely demonstrates how to obtain the host and a port, and does not use them for any type of protocol connection, such as nc or ssh. However, this code can easily be integrated into any CTF project that you have, allowing you to quickly and easily specify host and port into your program via commandline args. Although this code already does integrate with netcat, you can use this code to help with more advanced connections, if you modify the parameters as necessary. For example, in order to modify this code to work with SSH, you'll need to either specify a username and password, or use an identity file. For this, you'd simply have to add three lines of code below, one for each argument.")
    parser.add_argument('--host', type=str, required=False, help=' --host <host>       specify connection host')
    parser.add_argument('-p', type=int, required=False, help=' -p <port>        specify connection port')
    input_args = parser.parse_args()
    return input_args

user_args = parse_cmdline_args()

# print command-line args
for key, value in vars(user_args).items():
    print(f"{key}: {value}")


    
    
    
    # FOOTNOTES
    # argparse -h argument is hard-coded to --help by default, such that --help is the same thing as -h. In other words, don't try to add an argument for -h, because Python will complain about overriding
