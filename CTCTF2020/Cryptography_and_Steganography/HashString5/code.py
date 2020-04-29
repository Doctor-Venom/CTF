import hashlib
from random import randint
from string import ascii_letters
flag=open('flag.txt').read()
permuted_flag=''
for i,j in enumerate(flag):
    if i%2: permuted_flag=f'{permuted_flag}{j}{ascii_letters[randint(1,len(ascii_letters)-1)]}'
    else:permuted_flag = f'{j}{permuted_flag}{ascii_letters[randint(1,len(ascii_letters)-1)]}'
permuted_flag=permuted_flag.strip()
open('permuted_flag','w').write(permuted_flag)
hashed_flag= ''.join([hashlib.md5(i.encode()).hexdigest() for i in permuted_flag])
open('hashed_flag','w').write(hashed_flag)
