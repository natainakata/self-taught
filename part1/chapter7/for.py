#!/usr/bin/env python

name = "Ted"
for character in name:
    print(character)


shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)


tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)
