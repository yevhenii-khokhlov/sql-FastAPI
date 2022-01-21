import socket


def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
