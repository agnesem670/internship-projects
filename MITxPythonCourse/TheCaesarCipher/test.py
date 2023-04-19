alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = alphabet.upper()
chars = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
dictCesar = {}
shift = 3

# lowercase
for i in range (0, len(alphabet) - shift , 1):
    dictCesar[alphabet[i]] = alphabet[i+shift]
for i in range (len(alphabet) - shift, len(alphabet), 1):
    dictCesar[alphabet[i]] = alphabet[abs(len(alphabet)-i-shift)] 

# uppercase
for i in range (0, len(alphabetUpper) - shift , 1):
    dictCesar[alphabetUpper[i]] = alphabetUpper[i+shift]
for i in range (len(alphabetUpper) - shift, len(alphabetUpper), 1):
    dictCesar[alphabetUpper[i]] = alphabetUpper[abs(len(alphabetUpper)-i-shift)] 

# chars
for i in range (0, len(chars), 1):
    dictCesar[chars[i]] = chars[i]

# print (dictCesar)

# ----------------------------------------

# get message_text
# get dictCesar
message_text = "catAA../"
message_text_Cesar = []

for i in range (0, len(message_text)):
    message_text_Cesar.append(dictCesar[message_text[i]])

print ("".join(message_text_Cesar))