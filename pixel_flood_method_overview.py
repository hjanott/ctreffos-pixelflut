from src import basis

# get
get_message(3, 2)

# send
basis.send_pixel_int(4,4,255,22,33)
basis.send_pixel(4,4, "654312")
basis.send_message("PX 5 5 12DF56\n")