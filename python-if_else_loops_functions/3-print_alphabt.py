#!/usr/bin/python3
for ch in range(97, 123):
    if ch == "q" and ch == "e":
        continue
    print("{}" .format(chr(ch)), end="")
