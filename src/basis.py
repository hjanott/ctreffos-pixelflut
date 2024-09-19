import socket
import time

def send_message(message):
    ip_address = "192.168.188.106"
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(message.encode())
    print("send the pixel")
    
def send_pixel(x, y, rgb):
    message= f"PX {x} {y} " + rgb + "\n"
    send_message(message)
    
def send_pixel_int(x, y, r,g,b):
    send_pixel(x,y,f"{r:X}{g:X}{b:X}")