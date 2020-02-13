#Question 5 of Homework 1


p = 71
q = 97
e = 197
m = 8720

n = p * q
z = (p - 1) * (q - 1)
print(n)
print(z)
d = -1
for d in range(0, n):
    if (e*d % z) == 1:
        break
print(d)

encryptedMessage = (m**e) % n
value = encryptedMessage**d
print(value)
decryptedMessage = (encryptedMessage**d) % n
print(encryptedMessage)
print(decryptedMessage)