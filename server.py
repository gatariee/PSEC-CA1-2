from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
FTP_PORT = 2121
FTP_DIRECTORY = "./ftpServerData"

def main():
    authorizer = DummyAuthorizer()
    handler = FTPHandler
    handler.authorizer = authorizer
    authorizer.add_anonymous(FTP_DIRECTORY, perm="elradfmw") 
    handler.banner = "Welcome to PSEC FTP Server! "
    handler.passive_ports = range(60000, 65535)
    address = ('', FTP_PORT)
    server = FTPServer(address, handler)
    server.serve_forever()


if __name__ == '__main__':
    main()