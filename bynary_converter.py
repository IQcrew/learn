import struct
bynary_converter = lambda num: "".join(f"{i:08b}" for i in struct.pack(">d", num))
better_write = lambda x: f"{x[0]} {x[1:12]} {x[12:]}"
x = lambda y: print(better_write(bynary_converter(y)))


x(0.1+0.2)
x(0.3)






