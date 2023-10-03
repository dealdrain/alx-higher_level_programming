#!/usr/bin/python3

i = 0
for x in range(122, 96, -1):
    if x % 2 == 0:
        i = x
    else:
        i = x - 32
    print("{}".format(chr(i)), end='')
