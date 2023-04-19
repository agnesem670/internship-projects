# calculate the lowes monthly payment requaired to pay off dept in x months

def updateBalance (month, balance, annualInterestRate, minimumMonthlyPayment):
    """
    w: number of months (int)
    x: balace (int or float)
    y: annual interest rate (decimal)
    z: minimum monthly payment rate (int or float)

    return: update balance after x months of paying only minimum monthly payments
    """
    updBalance = 0

    for b in range (0, month):   
    
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if updBalance < balance:
            balance = updBalance
            month -= 1
            # print ("Month ", (b+1), " Remaining balance: ", round(balance,2) )
    return updBalance

   

month = 12
balance = 600
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minimumMonthlyPayment = monthlyPaymentRate * balance
epsilon = 0.01
answer = minimumMonthlyPayment
maximum = balance
lowestPayment = 0 # lowest monthly payment
loops_count=0 

upBalance = updateBalance(month, balance, annualInterestRate, answer)

while abs(upBalance) >= epsilon: # is looking for answer by compering updBalance(return) to epsilon (bisection search)
    if upBalance > 0: 
        minimumMonthlyPayment = answer
        answer = (minimumMonthlyPayment + maximum)/2

    else:
        maximum = answer
        answer = (minimumMonthlyPayment + maximum)/2

    upBalance = updateBalance(month, balance, annualInterestRate, answer)
    loops_count += 1

lowestPayment = answer
print (round (lowestPayment, 2), loops_count)

# print (updateBalance(month, balance, annualInterestRate, 360))