#!/usr/bin/python3
s = input("Address: ")
s = s.replace("0x", "")
for i in range(len(s), 0, -2):
    print("\\x" + s[i-2:i], end="")
print(f"\nReplace the out put of this in the EIP section of the details.\nDon't forget to set a breakpoint on your address (0x{s}) .\n CTRL + G, Then run ./7jmp_test.py")
