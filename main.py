import os
from portscanner import Scanner
from client import FTPHandler
while 1:
    print("*** PSEC Info Security Apps ***")
    print("1. Nmap Scanner")
    print("2. Upload/Download File using FTP")
    print("3. Send Custom Packet")
    print("4. Quit")
    choice = input(">> ")
    match choice:
        case '1':
            os.system('cls')
            hosts = "localhost"
            options = "-sU -sT --top-ports 10"
            ps = Scanner(targets = hosts, options = options)
            ps.run()
        case '2':
            os.system('cls')
            IP = '192.168.169.134'
            PORT = 2121
            conn = FTPHandler(IP, PORT)
            conn.run()
        case '3':
            print("custom")
        case '4':
            exit()
        case _:
            print("Invalid choice. Try again.")

# hosts = "localhost scanme.nmap.org"
# options = "-sU -sT --top-ports 10 -sV -sC --traceroute -O"