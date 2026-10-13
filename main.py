# Зчитування трьох шістнадцяткових рядків
msg1_hex = input().strip()
msg2_hex = input().strip()
msg3_hex = input().strip()

# Перетворення hex-рядків на масиви байтів
b1 = bytes.fromhex(msg1_hex)
b2 = bytes.fromhex(msg2_hex)
b3 = bytes.fromhex(msg3_hex)

# XOR між відповідними байтами: M = b1 ^ b2 ^ b3
decrypted_bytes = bytearray(x ^ y ^ z for x, y, z in zip(b1, b2, b3))

# Декодування результату у звичайний текст
print(decrypted_bytes.decode('ascii'))