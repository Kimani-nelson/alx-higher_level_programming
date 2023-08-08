#!/usr/bin/python3

for c in range(ord('a'), ord('z') + 1):
    if c != ord('q') and c != ord('e'):
        print(chr(c), end='')
print()  # To add a newline at the end
