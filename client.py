from ftplib import FTP 
import os
class FTPHandler:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.directory = "./ftpClientData"
    
    def connect(self):
        self.ftp = FTP()
        self.ftp.connect(self.ip, self.port)
        self.ftp.login()
    
    def listener(self):
        print("Type '?' for a full list of commands. '!' to quit.")
        while True:
            command = input(">> ")
            if command == '!':
                print("Closing connection...")
                self.ftp.quit()
                break
            elif command == '?':
                print("Commands: ls, get, put, clear, exit")
            elif command == 'ls':
                self.ftp.dir()
            elif command[:3] == 'get':
                if(len(command) == 3):
                    print("Usage: get <filename>")
                    continue
                filename = command[4:]
                if(filename not in self.ftp.nlst()):
                    print("File not found. ")
                    continue
                self.ftp.retrbinary(f"RETR {filename}", open(f"{self.directory}/{filename}", 'wb').write)
                print(f"File {filename} downloaded to {self.directory}/{filename}.")
            elif command[:3] == 'put':
                if(len(command) == 3):
                    print("Usage: put <filename>")
                    continue
                filename = command[4:]
                if(filename not in os.listdir(self.directory)):
                    print("File not found.")
                    continue
                self.ftp.storbinary(f"STOR {filename}", open(f"{self.directory}/{filename}", 'rb'))
                print(f"File {filename} uploaded to server.")
            elif command == 'clear':
                os.system('cls')
                print("Type '?' for a full list of commands. '!' to quit.")
            else:
                print("Command not recognized. Type '?' for a full list of commands. '!' to quit.")
    def run(self):
        print(f"Attempting connection to {self.ip}:{self.port}...")
        try:
            self.connect()
            print(f"Connected to: {self.ip}:{self.port}.\n")
            print(self.ftp.getwelcome())
            self.listener()
        except Exception:
            print(f"Connection to {self.ip}:{self.port} failed. \n")