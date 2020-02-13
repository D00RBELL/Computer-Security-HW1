#Question 4 of Homework 1

def remainder(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    for i in range(1, exponent + 1):
        result = (result * base) % modulus
    return result

value = remainder(3, 287, 23)
print(value)

value = 3**287 % 23
print(value)

