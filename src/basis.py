import socket
import time

def send_message(message):
    ip_address = "192.168.188.243"
    port = 1337
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(message.encode())
    print("send the pixel")
    
def send_pixel(x, y, rgb):
    message= f"PX {x} {y} " + rgb + "\n"
    send_message(message)