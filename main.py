import os
import socket
from termcolor import colored
from terminaltables import SingleTable
from portscanner import Scanner
from client import FTPHandler
from custom_packet import PacketHandler
clear = lambda: os.system('cls')
data = [
    ["1", "Port Scanner"], 
    ["2", "FTP Client"], 
    ["3", "Custom Packet"], 
    ["4", "Exit"]
]
options_table: SingleTable = SingleTable(data)
options_table.inner_row_border = 1
while 1:
    print(colored(
        rf"""
    ██████╗ ███████╗███████╗ ██████╗
    ██╔══██╗██╔════╝██╔════╝██╔════╝
    ██████╔╝███████╗█████╗  ██║     
    ██╔═══╝ ╚════██║██╔══╝  ██║     
    ██║     ███████║███████╗╚██████╗
    ╚═╝     ╚══════╝╚══════╝ ╚═════╝     
    {colored("Author: ", 'red', attrs=['bold'])} {colored("Zavier Lee", 'blue', attrs=['bold'])}   
    {colored("Class: ", 'red', attrs=['bold'])} {colored("DISM/FT/1B/05", 'blue', attrs=['bold'])}   
    {colored("Module Code: ", 'red', attrs=['bold'])} {colored("ST2414", 'blue', attrs=['bold'])}
    """, 'green').center(250))
    print(options_table.table)
    choice = input("\t>> ")
    match choice:
        case '1':
            clear()
            # hosts = "localhost scanme.nmap.org"
            options = "-sU -sT --top-ports 10 -sV -sC --traceroute -O"
            hosts = "scanme.nmap.org"
            # options = "-sU -sT --top-ports 10"
            ps = Scanner(targets = hosts, options = options)
            ps.run()
        case '2':
            clear()
            IP = socket.gethostbyname(socket.gethostname())
            PORT = 2121
            conn = FTPHandler(IP, PORT)
            conn.run()
        case '3':
            clear()
            ph = PacketHandler()
            ph.run()
        case '4':
            exit()
        case _:
            print("Invalid choice. Try again.")
    input("Press enter to continue...")