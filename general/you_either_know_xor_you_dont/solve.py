from itertools import *

sKey = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
skey = bytes.fromhex(sKey)
start = 'crypto{'

# find some information of the key
encrypt_start = bytes(b ^ ord(c) for b, c in zip(skey, start))

key = 'myXORkey'
print("".join(chr(b ^ ord(c)) for b, c in zip(skey, cycle(key))))