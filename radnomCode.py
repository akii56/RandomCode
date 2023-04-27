import random

text = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

code1 = ''.join((random.choice(text) for i in range(6)))
code2 = ''.join((random.choice(text) for i in range(6)))
code3 = ''.join((random.choice(text) for i in range(6)))
code4 = ''.join((random.choice(text) for i in range(6)))
code5 = ''.join((random.choice(text) for i in range(6)))



print("""
█▀█ ▄▀█ █▄░█ █▀▄ █▀█ █▀▄▀█   █▄▀ █▀█ █▀▄ █▀█ █░█ █
█▀▄ █▀█ █░▀█ █▄▀ █▄█ █░▀░█   █░█ █▄█ █▄▀ █▄█ ▀▄▀ █
""")



print(f'1.-------{code1}-------\n')
print(f'2.-------{code2}-------\n')
print(f'3.-------{code3}-------\n')
print(f'4.-------{code4}-------\n')
print(f'5.-------{code5}-------\n')










