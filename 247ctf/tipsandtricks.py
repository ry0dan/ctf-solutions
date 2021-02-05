#!/usr/bin/python3

from pwn import *
import re

io = remote('ea65cac93d1ef607.247ctf.com' , 50466)

print(io.recvline())
print(io.recvline())

for i in range(500):
   
      math = io.recvline().decode('utf-8')
      nums = re.findall(r'\d+',math)
       
      num1 = int(nums[0])
      num2 = int(nums[1])
       
      result = str(num1+num2)
      final = (result+'\r\n').encode('utf-8')
      io.sendline(final)
      io.recvline()
      print('the operation',i,'has been done with a',result)
      
print(io.recvline())
    
