#Importing modules 
import socket, sys
from thread import *

def main():
        # Declaring Program settings
        try:
            # Asking user for a listening port using
            listening_port = int(raw_input("[*] Enter Listening Port Number: "))
        expect KeyboardInterrupt: # Handles keyboard interrupts if the user wants to exit the script.
            print "\n[*] User Requested An Interrupt"
            print "[*] Application Exiting ..."
            sys.exit()
        
        max_conn  = 6 # Limit no. of connections to server Max = 6 
        buffer_size = 8192 # Max Socket Buffer Size
        