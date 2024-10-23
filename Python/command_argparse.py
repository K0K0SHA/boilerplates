# filename: command_parse_argparse.py
# author: K0K0$H@
# purpose: demonstrate how argparse can be used to parse optional command-line variables for host (string) and port (int)
########## This function can be used on anything that requires a host and a port. 

# sample usage 1: python3 command_parse_primitive.py -h challenge.ctf.org -p 2222
# sample usage 2: python3 command_parse.py --help
import argparse

def parse_cmdline_args():
    parser = argparse.ArgumentParser(description = "\n --h <host>       specify connection host\n --p <port>        specify connection port\n")
    parser.add_argument('--h', type=str, required=False, help='The host address (optional)')
    parser.add_argument('--p', type=int, required=False, help='The port number (optional)')
    parser.add_argument('--help', type=str, required=False, help='Display Help Page')
    input_args = parser.parse_args()
    return input_args

user_args = parse_cmdline_args()

# print command line args
for key, value in vars(user_args).items():
    print(f"{key}: {value}")
