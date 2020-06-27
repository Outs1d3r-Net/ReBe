import time

##=============
#DECRYPT
#=============
#GET THE PASSWORD DECRYPT CIPHER AND CONVERT TO BINARY
key = str(input("Enter the key: "))
bkey = bin(int.from_bytes(key.encode(), 'big'))[2:]

#GET THE SECRET MSG
msg = str(input("Enter the secret msg: "))

#DECONFUSION AND DEDIFUSION
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

msg = str(msg).replace(p[0], '0')
msg = str(msg).replace(p[1], '1')
msg = str(msg).replace(p[2], '2')
msg = str(msg).replace(p[3], '3')
msg = str(msg).replace(p[4], '4')
msg = str(msg).replace(p[5], '5')
msg = str(msg).replace(p[6], '6')
msg = str(msg).replace(p[7], '7')
msg = str(msg).replace(p[8], '8')
msg = str(msg).replace(p[9], '9')

#CONVERT HEX TO BIN
try:
    hmsg = hex(int(msg))[2:]
except ValueError:
    print("[*] ERRO ! INCORRET PASS OUR CIPHER FOR DECODE !\n")
    exit()
    

#CALC XOR
d1 = int(bkey, 2) ^ int(hmsg, 2)
d2 = d1.to_bytes((d1.bit_length() + 7) // 8, 'big').decode()

#SHOW
print("Decript MSG> ", d2)
time.sleep(5)