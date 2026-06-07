target = b'libtts.so: Using default dictionary name\n'
replacement = b'\r\x1b[K' + (b'\x00' * (len(target) - 4))
filepath = 'libtts_us.so'

with open(filepath, 'rb') as f:
    content = f.read()

content = content.replace(target, replacement)

with open(filepath, 'wb') as f:
    f.write(content)