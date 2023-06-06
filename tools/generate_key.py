from random import choice

chars = "ABCDEFGHIJKLMOPQURSTVWXYZ"

characters = list(chars) + list(chars.lower()) + list("1234567890")

key = "".join([choice(characters) for x in range(30)])

print(key)