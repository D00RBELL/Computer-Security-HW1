#Question 1 of Homework 1

ciphertext = 'OBRGXIMYAZZAWCATBNMUYYHAZNVGFCXPVVSIJSVLKIFAVGBIECAZSBWGRGRQWUCHMMOCYEFLGQQNKFSHQMGYALNKCIJQVEKVWXNFOYFYQBESGOYTXMAYTXSISNBPMSGOJBKFWRUTTMLSBNQMLLRGFNZUAWHZLBRVZGHUVZMCKJEHSLSWGXCNZYEXRIMLPXRIXNUXRNSNRPHFDHBMAYWKHTKNGNUXRNJUVGMYNYEYNLYYGPGYFSBNQQWUCHMMSLRWTFDYQRNOJUEWNLVUZIDHWXLHTLKNEXMALBRQGUMMGXCUFXLHTLLLRTROJYFIDHLIGADLUBVXENSCALVCDFFIQCFAHISILUXXZXNUAMZAWISRNOJYKMQYECGRSBWHAHLUFBBPDPWLJBRYOCYEAYSVYXSISPRKSNZYPHMMWKHXMWWMGAZNEOFMDHKORMGOKNUHTAZQRAZPWBRTQXGZFMTJAXUTRNWCAPZLUFRODLFYFLGUKHRODLTYRGRYWHNLRIUCNMDXOCGAKIFAQXKUQMVGZFDBVLSIJSGADLWCFGNCFMGTMWWISTBIMHGKXBSPVGFVWHRYHNWXSKNGHLBENHYYQPZLXUEXNHDSBGDQZIXGNQKNUXCCKUFMQIMMRYEYUNFHEUDIAZVUJWNGQYSFVSDNZYFNOLWGRBLJGLGTMWWISKZJAXVMXCFVEBMAAHTBSNGUPENMWCGBRIFFLHMYOBBBRNZIEHTAZFLTBKMUVGSYVQVMGNZYROHFKISPZLOBBVZHLBBKNOYBYRTHVYELSUFXGADJJISBSUTFRPZSGZPTQLQCAZHNGHGADMCCYEEODARGDLSFQHDMFIGKZCKYNLDWGHQEDPQHRBSBWLNKDBAMFNOJDSJTFIFMYHZXWXZHQYLBNGSQAWRHMWWQNKHMVYPEZLWXUXVCDFAHSQSMGXOLWWVHTMLCZXHHOUVMHHYZBKQYAHSHQWWGRGSMFIEPHFDBRMTLFBVLZLESOTBEXIEYQYKBFNOJDCRLAOLWEHRMWMGADYFYZRRZJIAMHYJQVMGIMNQXKUQNUXUUDORHENAGRMGULCFUDCFANEHNLFRTGYSXBYXIMLBIOIFYAMGUKWBNMNWXSHQGGLRMGUFYVMGYJHHFDLAWNEROHYEBNLANLHQNZYABBYKNPTKWMFNMHIFMJBSBJYTTQXLIPHLGAMFTQCSN'

#This splits the cipher into sections of three to be compared with other sections to determine the length of the key
cipherlist = []
for i in range(0, len(ciphertext), 3):
    cipherlist.append(ciphertext[i:i+3])

#This does the comparison of each individual three letter section to find the duplicates
for i in range(0, len(cipherlist)):
    for j in range(0, len(cipherlist)):
        if cipherlist[i] == cipherlist[j] and not i == j:
            output = cipherlist[i] + ' ' + str(j*3)
            print(output)

#from the results above, the length of the key can be found by finding a common divisor for all of the duplicates
#this is found to be either 3 or 6, so from there, a frequency analysis can be done on each section of 3 or six letters
#to find the individual letters in the key

#frequency analysis for key length of 3
string1 = []
string2 = []
string3 = []
key1 = []
key2 = []
key3 = []
value = 0
for i in range(0, 26):
    key1.append(0)
    key2.append(0)
    key3.append(0)

for i in range(0, len(ciphertext) - 3, 3):
    string1.append(ciphertext[i])
    string2.append(ciphertext[i + 1])
    string3.append(ciphertext[i + 2])

for i in string1:
    value = ord(i) - 65
    key1[value] += 1

for i in string2:
    value = ord(i) - 65
    key2[value] += 1

for i in string3:
    value = ord(i) - 65
    key3[value] += 1

print(key1)
print(key2)
print(key3)

#frequency analysis for key length of 6
string1 = []
string2 = []
string3 = []
string4 = []
string5 = []
string6 = []
key1 = []
key2 = []
key3 = []
key4 = []
key5 = []
key6 = []
value = 0
for i in range(0, 26):
    key1.append(0)
    key2.append(0)
    key3.append(0)
    key4.append(0)
    key5.append(0)
    key6.append(0)

for i in range(0, len(ciphertext) - 6, 6):
    string1.append(ciphertext[i])
    string2.append(ciphertext[i + 1])
    string3.append(ciphertext[i + 2])
    string4.append(ciphertext[i + 3])
    string5.append(ciphertext[i + 4])
    string6.append(ciphertext[i + 5])

for i in string1:
    value = ord(i) - 65
    key1[value] += 1

for i in string2:
    value = ord(i) - 65
    key2[value] += 1

for i in string3:
    value = ord(i) - 65
    key3[value] += 1

for i in string4:
    value = ord(i) - 65
    key4[value] += 1

for i in string5:
    value = ord(i) - 65
    key5[value] += 1

for i in string6:
    value = ord(i) - 65
    key6[value] += 1


print('')
print(key1)
print(key1.index(max(key1)) - 4)
print(key2)
print(key2.index(max(key2)) - 4)
print(key3)
print(key3.index(max(key3)) - 4)
print(key4)
print(key4.index(max(key4)) - 4)
#The second highest would be T and this better fits the key in the end because of words in the english language
print(key5)
if key5.index(max(key5)) < 4:
    print(key5.index(max(key5)) + 22)
else:
    print(key5.index(max(key5)) - 4)
#there are two maxes in this and due to the max function, the second one gets ignored, but again this one fits the key better
print(key6)
print(key6.index(max(key6)))

key = 'SUNTZU'
origtext = []
#this results in the key being SUNTZU or Sun Tzu which is the author of The Art of War
#From here, it is just a matter of using the key to decrypt the ciphertext to get the plaintext

#generates the key for the length of the ciphertext
key = list(key)
if(len(ciphertext) != len(key)):
    for i in range(len(ciphertext) - len(key)):
        key.append(key[i % len(key)])
print(ciphertext)
for i in range(0, len(ciphertext)):
    x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
    x += ord('A')
    origtext.append(chr(x))
plaintext = '' . join(origtext)
print(plaintext)

#the new plaintext  is a passage from Sun Tzu's The Art of War and it is an accurate copy because of the key