import socket

def gethostname():
    return socket.gethostname()

def getlocaladdress():
    return socket.gethostbyname(socket.gethostname())
