import time

#=============
#ENCRYPT
#=============
#GET THE KEY CIPHER AND CONVERT TO BIN
key = str(input("Enter the key: "))
bkey = bin(int.from_bytes(key.encode(), 'big'))[2:] 

#GET THE MSG CIPHER AND CONVERT TO BIN
msg = str(input("Enter the secret msg: "))
bmsg = bin(int.from_bytes(msg.encode(), 'big'))[2:]  

#CALC XOR IN VARIABLES AND CONVERT TO HEX
smsg = int(bkey, 2) ^ int(bmsg, 2)
smsg = bin(smsg)[2:]
smsg = int(smsg, 16)

#CONFUSION AND DIFUSION
alfa = []
for i in range(65, 91):
    alfa.append(chr(i).lower())

alfa = ''.join(alfa)
m = hex(int(bkey))[2:]

#MODULE LEN(ALPHABET)
mod = int(len(alfa))
num = int(len(m))
count = 1
while mod < num:
    mod = int(len(alfa)) * count
    count = count + 1
mod = mod - int(len(alfa))
mod = num - mod

#MUTATION
a = alfa[len(str(mod))]
p = str(alfa).split(a)[::-1]
p = ''.join(p)[:10]

smsg = str(smsg).replace('0', p[0])
smsg = str(smsg).replace('1', p[1])
smsg = str(smsg).replace('2', p[2])
smsg = str(smsg).replace('3', p[3])
smsg = str(smsg).replace('4', p[4])
smsg = str(smsg).replace('5', p[5])
smsg = str(smsg).replace('6', p[6])
smsg = str(smsg).replace('7', p[7])
smsg = str(smsg).replace('8', p[8])
smsg = str(smsg).replace('9', p[9])

#SHOW
print("Encript MSG> ", smsg)
time.sleep(5)

