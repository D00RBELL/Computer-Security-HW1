#Question 2 of Homework 1

letterFrequency = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }
plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
plaintext = plaintext.upper()
sum = sum(letterFrequency.values())
mean = sum / 26
variance = 0

for i in letterFrequency:
    variance += (letterFrequency[i] - mean)**2
variance /= 26
print("English Frequency Variance")
print(variance)

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
    variance /= 26
    return(variance)

print("Plaintext Frequency Variance")
variance = varianceFinder(plaintext)
print(variance)

def keyGenerator(plaintext, key):
    key = list(key)
    if (len(plaintext) != len(key)):
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryptText(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        x += ord('A')
        ciphertext.append(chr(x))
    return("" . join(ciphertext))

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