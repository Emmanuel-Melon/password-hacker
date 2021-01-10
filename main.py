from socket_connection import client_socket
import argparse

parser = argparse.ArgumentParser(description="Password hacker demo")

# command line arguments
parser.add_argument("-ip", "--ip_address")
parser.add_argument("-p", "--port")
parser.add_argument("-m", "--message")

args = parser.parse_args()


message = args.message.encode()

# send message via socket
