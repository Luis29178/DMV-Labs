##Caesar Cipher
MSG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROT = 13

for x in MSG:
    c = ord(x)
    b = c - 64
    
    if b < 14:
        v = b + ROT
        print(v)
    else:
        v = b + (ROT -26)
        print(v)
   
    
   
       
    
   
   


