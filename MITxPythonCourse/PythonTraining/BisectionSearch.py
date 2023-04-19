# guess = 25
# epsilon = 0.01
# guess_num = 0
# high = guess
# low = 0
# ans = (low + high)/ 2

# while abs(ans**2 - guess) >= epsilon:
#     guess_num +=1
#     if ans**2 < guess:
#         low = ans
#     else:
#         high = ans
#     ans = (low + high)/ 2
# print (ans)   
# print (guess_num) 

low = 0
high = 100
answ = int ((low + high)/2)
guess = 'h'

print ("Please think of a number between 0 and 100!")
while guess != "c":
    guess = input ("Is your secret number " + str(answ) + " ?\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if guess == 'h':
        high = answ
        answ = int ((low + high)/2)
    if guess == "l":
        low = answ
        answ = int ((low + high)/2)
    if guess == "c":
        print ("Game over. Your secret number was:" + str(answ))
    if guess != "h" and guess != "l" and guess != "c":
        print ("Sorry, I did not understand your input")
