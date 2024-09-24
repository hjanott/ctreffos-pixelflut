from src import basis
from random import randint
import time

width=10
height=10

for x in range(0, width):
    for y in range(0, height):
        print(f'{x},{y}')
        basis.send_pixel(x,y, '000000')

catch = {}
try:
    while True:
        x = randint(0 , width-1)
        y = randint(0 , height-1)
        print(f'{x},{y}')
        basis.send_pixel(x,y, 'FFFFFF')
        time.sleep(1)
        color = basis.get_hex_color(x, y)
        if color != 'FFFFFF':
            print(f'{color}')
            catch[color] = catch.get(color, 0) + 1
            for i in range(3):
                basis.send_pixel(x, y, '000000')
                time.sleep(0.1)
                basis.send_pixel(x, y, color)
                time.sleep(0.1)
            basis.send_pixel(x, y, '000000')
        else:
            basis.send_pixel(x, y, '000000')
except KeyboardInterrupt:
    print('')
    for color, count in catch.items():
        print(f'{color}: {count}')
