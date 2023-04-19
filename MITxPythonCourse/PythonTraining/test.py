s = "aleniokonadeott"
numb_of_vowels = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o":
        numb_of_vowels += 1
print ("Number of vowels: " + str(numb_of_vowels))

# ====================================
# s = "ksjhfbobbobkjabosbdbf"
# letter_count = 0
# bob_numb = 0
# for letter in s:
#     letter_count +=1

#     bob_count = letter_count

#     if letter == "b":
#         if s[bob_count] == "o":
#             bob_count += 1
#             if s[bob_count] == "b":
#                 bob_numb += 1

# print (bob_numb)

#=======================================
# s = "ksjhfbobbobkjabosbdbf"
# letter_count = 0
# bob_numb = 0

# for letter in s:
#     letter_count += 1
#     if letter == "b" and s[letter_count] == "o" and s[letter_count+1] == "b":
#         bob_numb += 1

# print(bob_numb)

# ======================================
# s = "ksjhfbobbobkjabosbdbf"
# wordToFind = "bob"

# bob_numb = 0
# wordLenght = len(wordToFind)

# for i in range(len(s)-wordLenght+1):
#     if s[i:wordLenght+i] == wordToFind:
#         bob_numb += 1

# print(bob_numb)

# ======================================
# word = "wzabdeef"
# alphabet = "abcdefghijklmnopqrstuwxyz"

# longest = 0
# current_count = 0

# for letter in word:
#     if word.index (letter) == 0:
#         current_count += 1
#     if word.index (letter) > 0:
#         prev_letter = word [word.index (letter) -1]
#         if alphabet.index (letter) > alphabet.index (prev_letter):
#             current_count += 1
#         else:
#             current_count = 1
#     if current_count > longest:
#         longest = current_count
# print (longest)

# ===================================
# word = "wzabdeewj"
# alphabet = "abcdefghijklmnopqrstuwxyz"

# longest = 0
# current_count = 0

# for l in range (0, len(word)):
#     if l == 0:
#         current_count += 1
#     if l > 0:
#         current_letter = word [l]
#         prev_letter = word [l -1]
#         if alphabet.index (current_letter) >= alphabet.index (prev_letter):
#             current_count += 1
#         else:
#             current_count = 1
#     if current_count > longest:
#         longest = current_count
# print (longest)


#======================================
# - w poniższym operujesz na indeksach stringów, a nie na samych literach
# - mieszanie indeksów i liter (for in) jest raczej niezdrowe - nieczytelne i można się samemu oszukać
# - niestety w pythonie pętla for jest bardzo okrojona w stosunku do innych programów, przez co trzeba się męczyć z dostosowaniem do swoich potrzeb samej pętli
# a nie z rozwiązaniem zadania (ale pewnie twórcy i fani będą usprawiedliwiali to tym, że przez to jest mniej błędów - fakt jest taki, że jeden problem zastąpiono
# drugim)
#
# Jedna z zasad: im bradziej uniwersalny i krótki kod, tym jego sens jest trudniejszy do odkrycia, dla tego dawaj chociaż krótkie komentarze - po tygodniu 
# nawet twój własny kod wygląda jakby pisała go obca osoba.

# prezstawiłem ci interaktywną konsolę na shift+F5
# shift+alt+i z zaznaczoną zmienną wstawia ją do watcha



# word = "afaaaabdaaa"
# alphabet = "abcdef"

# i=0
# alphPrevIndex = 0
# subLongest = 0
# longest = 0

# #dla każdej  litery w zmiennej 'word' (przy czym 'i' jest indeksem litery, a nie samą literą)
# while i < len(word):
#     #weź indeks tej litery w ciągu 'alphabet'
#     alphCurrIndex = alphabet.index(word[i])
#     #jeżeli ten index jest większy lub równy od poprzedniego (czyli litera jest taka sama bądź kolejna w ciągu 'alphabet' czyli NIE POPRZEDNIA z ciągu 'alphabet')
#     if alphCurrIndex >= alphPrevIndex:
#         #poprzesuwaj indeksy i poustawiaj rezultaty (jeśli trzeba)
#         alphPrevIndex = alphCurrIndex
#         subLongest += 1
#         if subLongest > longest:
#             longest = subLongest
#         #przesuń indeks do następnej litery w 'word'
#         i += 1
#     #jeśli nie, to zeruj liczniki (po wyjściu z if, zaczniesz od indeksu na którym skończyłaś obecny if)
#     else:
#         alphPrevIndex = 0
#         subLongest = 0

# print(longest)

# ========================

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])

print (isIn("z", "abdfghklomprq"))