# Question 2 of Homework 1

#part a, english language frequency variance and plaintext frequency variance
letterFrequency = {"A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
                   "G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
                   "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
                   "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
                   "Y": .01974, "Z": .00074}
plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
plaintext = plaintext.upper()
sum = sum(letterFrequency.values())
mean = sum / 26
variance = 0

for i in letterFrequency:
    variance += (letterFrequency[i] - mean) ** 2
variance /= 26
print("English Frequency Variance")
print(variance)

#finds each letter frequency in a certain text, then finds the overall variance of the text
def varianceFinder(plaintext):
    total = 0
    variance = 0
    plaintextFrequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0,
                          "L": 0,
                          "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0,
                          "X": 0, "Y": 0, "Z": 0}
    for i in plaintext:
        plaintextFrequency[i] += 1
        total += 1
    for i in plaintextFrequency:
        plaintextFrequency[i] /= total
        variance += plaintextFrequency[i]

    mean = variance / 26
    variance = 0

    for i in plaintextFrequency:
        variance += (plaintextFrequency[i] - mean) ** 2
    #print(plaintextFrequency)
    variance /= 26
    return (variance)


print("Plaintext Frequency Variance")
variance = varianceFinder(plaintext)
print(variance)

#Part b, variance of different ciphertexts

#Generates a string that is the key duplicated to be the same length as the plaintext for encryption or decryption
def keyGenerator(plaintext, key):
    key = list(key)
    if (len(plaintext) != len(key)):
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

#Encrypts the plaintext with the given key using a Vigenere cipher
#this function assumes that plaintext and key are the same length
def encryptText(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        x += ord('A')
        ciphertext.append(chr(x))
    return ("".join(ciphertext))


yzkey = keyGenerator(plaintext, 'YZ')
xyzkey = keyGenerator(plaintext, 'XYZ')
wxyzkey = keyGenerator(plaintext, 'WXYZ')
vwxyzkey = keyGenerator(plaintext, 'VWXYZ')
uvwxyzkey = keyGenerator(plaintext, 'UVWXYZ')

yztext = encryptText(plaintext, yzkey)
xyztext = encryptText(plaintext, xyzkey)
wxyztext = encryptText(plaintext, wxyzkey)
vwxyztext = encryptText(plaintext, vwxyzkey)
uvwxyztext = encryptText(plaintext, uvwxyzkey)
print()
print("yz Frequency Variance")
variance = varianceFinder(yztext)
print(variance)
print("xyz Frequency Variance")
variance = varianceFinder(xyztext)
print(variance)
print("wxyz Frequency Variance")
variance = varianceFinder(wxyztext)
print(variance)
print("vwxyz Frequency Variance")
variance = varianceFinder(vwxyztext)
print(variance)
print("uvwxyz Frequency Variance")
variance = varianceFinder(uvwxyztext)
print(variance)


#part c, mean variance with different ciphetext

caesarU = []
caesarV = []
caesarW = []
caesarX = []
caesarY = []
caesarZ = []
varianceU = 0
varianceV = 0
varianceW = 0
varianceX = 0
varianceY = 0
varianceZ = 0
mean = 0

for i in range(0, len(yztext), 2):
    caesarY.append(yztext[i])
    caesarZ.append(yztext[i + 1])

caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ) / 2
print()
print("YZ mean variance")
print(mean)

caesarY = []
caesarZ = []
for i in range(0, len(xyztext), 3):
    caesarX.append(xyztext[i])
    caesarY.append(xyztext[i + 1])
    caesarZ.append(xyztext[i + 2])

caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX) / 3
print("XYZ mean variance")
print(mean)

caesarX = []
caesarY = []
caesarZ = []
for i in range(0, len(wxyztext), 4):
    caesarW.append(wxyztext[i])
    caesarX.append(wxyztext[i + 1])
    caesarY.append(wxyztext[i + 2])
    caesarZ.append(wxyztext[i + 3])

caesarW = "".join(caesarW)
caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceW = varianceFinder(caesarW)
varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX + varianceW) / 4
print("WXYZ mean variance")
print(mean)

caesarW = []
caesarX = []
caesarY = []
caesarZ = []
for i in range(0, len(vwxyztext), 5):
    caesarV.append(vwxyztext[i])
    caesarW.append(vwxyztext[i + 1])
    caesarX.append(vwxyztext[i + 2])
    caesarY.append(vwxyztext[i + 3])
    caesarZ.append(vwxyztext[i + 4])

caesarV = "".join(caesarV)
caesarW = "".join(caesarW)
caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceV = varianceFinder(caesarV)
varianceW = varianceFinder(caesarW)
varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX + varianceW + varianceV) / 5
print("VWXYZ mean variance")
print(mean)

caesarV = []
caesarW = []
caesarX = []
caesarY = []
caesarZ = []
for i in range(0, len(uvwxyztext), 6):
    caesarU.append(uvwxyztext[i])
    caesarV.append(uvwxyztext[i + 1])
    caesarW.append(uvwxyztext[i + 2])
    caesarX.append(uvwxyztext[i + 3])
    caesarY.append(uvwxyztext[i + 4])
    caesarZ.append(uvwxyztext[i + 5])

caesarU = "".join(caesarU)
caesarV = "".join(caesarV)
caesarW = "".join(caesarW)
caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceU = varianceFinder(caesarU)
varianceV = varianceFinder(caesarV)
varianceW = varianceFinder(caesarW)
varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX + varianceW + varianceV + varianceU) / 6
print("UVWXYZ mean variance")
print(mean)
print()

#part d, mean variance of one ciphertext assuming different key lengths

caesarU = []
caesarV = []
caesarW = []
caesarX = []
caesarY = []
caesarZ = []

for i in range(0, len(uvwxyztext), 2):
    caesarY.append(uvwxyztext[i])
    caesarZ.append(uvwxyztext[i + 1])

caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ) / 2
print("UVWXYZ mean variance assuming key length 2")
print(mean)


caesarX = []
caesarY = []
caesarZ = []

for i in range(0, len(uvwxyztext), 3):
    caesarX.append(uvwxyztext[i])
    caesarY.append(uvwxyztext[i + 1])
    caesarZ.append(uvwxyztext[i + 2])

caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX) / 3
print("UVWXYZ mean variance assuming key length 3")
print(mean)


caesarX = []
caesarY = []
caesarZ = []

for i in range(0, len(uvwxyztext), 4):
    caesarW.append(uvwxyztext[i])
    caesarX.append(uvwxyztext[i + 1])
    caesarY.append(uvwxyztext[i + 2])
    caesarZ.append(uvwxyztext[i + 3])

caesarW = "".join(caesarW)
caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceW = varianceFinder(caesarW)
varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX + varianceW) / 4
print("UVWXYZ mean variance assuming key length 4")
print(mean)


caesarW = []
caesarX = []
caesarY = []
caesarZ = []

for i in range(0, len(uvwxyztext), 5):
    caesarV.append(uvwxyztext[i])
    caesarW.append(uvwxyztext[i + 1])
    caesarX.append(uvwxyztext[i + 2])
    caesarY.append(uvwxyztext[i + 3])
    caesarZ.append(uvwxyztext[i + 4])

caesarV = "".join(caesarV)
caesarW = "".join(caesarW)
caesarX = "".join(caesarX)
caesarY = "".join(caesarY)
caesarZ = "".join(caesarZ)

varianceV = varianceFinder(caesarV)
varianceW = varianceFinder(caesarW)
varianceX = varianceFinder(caesarX)
varianceY = varianceFinder(caesarY)
varianceZ = varianceFinder(caesarZ)
mean = (varianceY + varianceZ + varianceX + varianceW + varianceV) / 5
print("UVWXYZ mean variance assuming key length 5")
print(mean)