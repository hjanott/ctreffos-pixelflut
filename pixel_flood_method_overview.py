from src import basis

# send
basis.send_pixel_int(4,4,255,22,33)
basis.send_pixel(4,4, "654312")
basis.send_message("PX 5 5 12DF56\n")

# get
print(basis.get_color(4, 4))
print(basis.get_hex_color(4, 4))