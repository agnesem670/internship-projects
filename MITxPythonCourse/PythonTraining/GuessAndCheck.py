# x = int (input ("Enter a number: "))
# answ = 0

# while answ ** 3 < x:
#     answ += 1

# if answ ** 3 != x:
#     print ("Wrong number")
# else:
#     print ("A cube root of " + str (x) + " is " + str(answ))

# cube = 27
# for x in range (cube+1):
#     if x ** 3 == cube:
#         print ("A cube root of " + str (cube) + " is " + str(x))

# cube = -28
# for x in range (abs (cube)+1):
#     if x ** 3 >= abs(cube):
#         break
# if x ** 3 != abs(cube):
#     print ("It's not a perfect cube")
# else:
#     if cube <0:
#         x = -x
#     print ("A cube root of " + str (cube) + " is " + str(x))

# cube = 29
# guess = 0.0
# i = 0.001
# epsilon = 0.01
# num_guesses = 0

# while abs (guess**3 - cube) >= epsilon and guess <= cube:
#     num_guesses += 1
#     guess += i
# print ("Number of guesses is: ", num_guesses)
# if guess**3 - cube >= epsilon:
#     print ("Failed on cube root of")
# else:
#     print ("Cube root of ", cube, " is ", guess)
   
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    print( abs(guess**2 -x))
    if abs(guess**2 -x) >= epsilon:
        guess += step


# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))