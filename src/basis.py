import socket

ip_address = "192.168.188.246"
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))

def send_message(message: str) -> None:
    """sends a pixel in the message coordinates and RGB color. format needs to be 'PX X Y RGB'"""
    s.sendall(message.encode())
    print("send the pixel")
    
def send_pixel(x: int, y: int, rgb: str) -> None:
    """sends a pixel in the RGB color"""
    message= f"PX {x} {y} " + rgb + "\n"
    send_message(message)
    
def send_pixel_int(x: int, y: int, r: int, g: int, b: int) -> None:
    """sends a pixel in the RGB color"""
    send_pixel(x,y,f"{r:X}{g:X}{b:X}")

def get_hex_color(x: int, y: int) -> str:
    """gets a pixels RGB color as hex string"""
    message = f'PX {x} {y}\n'
    s.sendall(message.encode())
    #Länge vom String + Leerzeichen + RGB-Hexcode)
    expected_message_length = len(f'{message} ffffff'.encode())
    response = b""
    while len(response) < expected_message_length:
        response += s.recv(expected_message_length)
    return response.decode().split()[3]

def get_color(x: int, y: int) -> tuple[int, int, int]:
    """gets a pixels rgb color as RGB decimal numbers"""
    response = get_hex_color(x, y)
    r = int(response[0:2], 16)
    g = int(response[2:4], 16)
    b = int(response[4:6], 16)
    return r, g, b
