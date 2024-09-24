from src import basis

width=10
height=10

for x in range(0, width):
    for y in range(0, height):
        print(f'{x},{y}')
        basis.send_pixel(x,y, '000000')
