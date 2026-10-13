sKey = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
skey = bytes.fromhex(sKey)

for i in range(256) :
    out = bytes(b ^ i for b in skey)
    if out.startswith(b'crypto{') :
        print(i, out)
