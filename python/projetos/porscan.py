import socket
import sys

ip = sys.argv[1]
meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for porta in range(65535):
    if meu_socket.connect_ex((ip, porta)) == 0:
        print("Prta", porta, " [ABERTA]")
    meu_socket.close()
