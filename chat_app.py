import threading
import socket
import os
import pyfiglet  

os.system("cls")
os.system("color 6")

out = pyfiglet.figlet_format("\t\t UDP CHAT APP", font = "digital" )
print(out)

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

reciever_ip = "192.168.43.254"
rec_port = 1111

ip = "192.168.43.116"
port = 2222

s.bind((ip , port))

def recv_msg():
    while True:
        r_msg = s.recvfrom(1024)
        data = r_msg[0].decode()
        sender = r_msg[1][0]
        print("\n\t\t\t\t", sender + " : " + data)


def send_msg():
    while True:
        msg = input("")
        s.sendto(msg.encode(), (reciever_ip , rec_port ))


send_msg = threading.Thread(target=send_msg)
recv_msg = threading.Thread(target=recv_msg)

recv_msg.start()
send_msg.start()
