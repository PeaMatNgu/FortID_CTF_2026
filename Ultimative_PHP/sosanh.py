import hashlib
import re

magic = re.compile(rb"^0+e[0-9]+$")

for i in range(100_000_000):
    code = str(i)
    material = b"ULTIMATIVE-PHP-2026:" + code.encode()

    legacy = hashlib.md5(material).hexdigest()[:9].encode()
    modern = hashlib.sha256(material).hexdigest()[:9].encode()

    if (
        legacy != modern
        and magic.fullmatch(legacy)
        and magic.fullmatch(modern)
    ):
        print("FOUND")
        print("code  =", code)
        print("legacy =", legacy.decode())
        print("modern =", modern.decode())
        break

    if i % 1_000_000 == 0:
        print("checked:", i)
