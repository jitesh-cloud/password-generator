# Python Project on Generation of a Secure Stroong Password
# Random module is used for random selection of characters
import random

# characters is a string containing all the characters used to make a random password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"

# length defines the actual required length that user needs
length = int(input("Password Length Requried: "))
password = ''

# random.choice() accepts iterable
# In the loop it throws out single character on random play
# Code runs for the n times where n is length
for i in range(length):
    password += random.choice(characters)

# finally interprets a result : final password
print(password)
