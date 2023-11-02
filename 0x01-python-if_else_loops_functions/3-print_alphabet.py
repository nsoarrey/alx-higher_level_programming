#!/bin/python3
for number in range(97, 123):
    if(number == 113 or number == 101):
        continue
    print(chr(number), end=" ")
