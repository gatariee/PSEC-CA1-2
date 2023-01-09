from scapy.all import send, IP, TCP, ICMP, UDP
from terminaltables import SingleTable
import os
class PacketHandler:
    def __init__(self):
        self.source_ip = ""
        self.destination_ip = ""
        self.source_port = 0
        self.destination_port = 0
        self.protocol = ""
        self.payload = ""
    def send_packet(self):
        if self.protocol == "TCP":
            packet = IP(src=self.source_ip, dst=self.destination_ip)/TCP(sport=self.source_port, dport=self.destination_port)/self.payload
        elif self.protocol == "UDP":
            packet = IP(src=self.source_ip, dst=self.destination_ip)/UDP(sport=self.source_port, dport=self.destination_port)/self.payload
        elif self.protocol == "ICMP":
            packet = IP(src=self.source_ip, dst=self.destination_ip)/ICMP()/self.payload
        send(packet)
    def generate_table(self):
        table_data = [
            ["", "OPTION", "VALUE"], 
            ["1", "Source IP", self.source_ip],
            ["2", "Destination IP", self.destination_ip],
            ["3", "Source Port", self.source_port],
            ["4", "Destination Port", self.destination_port],
            ["5", "Protocol", self.protocol],
            ["6", "Payload", self.payload]
        ]
        TABLE = SingleTable(table_data)
        TABLE.inner_row_border = 1
        print(TABLE.table)
    def send_input(self, option: int):
        match option:
            case 1:
                self.source_ip = input("Enter the source IP: ")
            case 2:
                self.destination_ip = input("Enter the destination IP: ")
            case 3:
                self.source_port = int(input("Enter the source port: "))
            case 4:
                self.destination_port = int(input("Enter the destination port: "))
            case 5:
                self.protocol = input("Enter the protocol: ")
            case 6:
                self.payload = input("Enter the payload: ")
    def validate_input(self, option: int) -> bool:
        try:
            option = int(option)
        except ValueError:
            return False
        match option:
            case 1:
                return True
            case 2:
                return True
            case 3:
                return True
            case 4:
                return True
            case 5:
                return True
            case 6:
                return True
            case _:
                return False
    def run(self):
        while True:
            os.system('cls')
            self.generate_table()
            print("Enter the option you want to change. Enter '!'' to send the packet.")
            option = input(">> ")
            if option == "!":
                self.send_packet()
                break
            else:
                if self.validate_input(option):
                    self.send_input(int(option))
                else:
                    print("Invalid option. Try again.")
                    input("Press enter to continue...")

if __name__ == "__main__":
    packet = PacketHandler()
    packet.run()



