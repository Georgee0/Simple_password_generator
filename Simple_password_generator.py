# python3
# Simple random password generator

import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '()_+-={}[]:;?.,<>''""'

all = lower + upper + numbers + symbols 

length = 15 # length of pasword to be generated 

pasword_generated = ''.join(random.sample(all, length))

print(pasword_generated)