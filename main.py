import os
import socket
from termcolor import colored
from terminaltables import SingleTable
from portscanner import Scanner
from client import FTPHandler
from custom_packet import PacketHandler
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input("Press enter to continue...")

def main_menu():       
    data = [
        ["1", "Port Scanner"], 
        ["2", "FTP Client"], 
        ["3", "Custom Packet"], 
        ["4", "Exit"]
    ]
    options_table: SingleTable = SingleTable(data)
    options_table.inner_row_border = 1
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


while 1:
    clear_screen()
    main_menu()
    choice = input(">> ")
    match choice:
        case '1':
            clear_screen()
            # hosts = "localhost scanme.nmap.org"
            # options = "-sU -sT --top-ports 10 -sV -sC --traceroute -O"
            hosts = "scanme.nmap.org"
            options = "-sU -sT --top-ports 10"
            nmap_scan = Scanner(targets = hosts, options = options)
            nmap_scan.run()
            buffer()
        case '2':
            clear_screen()
            IP = socket.gethostbyname(socket.gethostname())
            PORT = 2121
            ftp_client = FTPHandler(IP, PORT)
            ftp_client.run()
            buffer()
        case '3':
            clear_screen()
            packet_handler = PacketHandler()
            packet_handler.run()
            buffer()
        case '4':
            exit()
        case _:
            print("Invalid choice. Try again.")