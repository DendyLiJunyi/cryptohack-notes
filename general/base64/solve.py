import base64
key = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
decode = bytes.fromhex(key)
encode = base64.b64encode(decode)
print(encode)