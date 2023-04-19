balance = 5000     # the outstanding balance on the credit card
annualInterestRate = 0.2  # annual interest rate as a decimal
monthlyPaymentRate = 0.04  # minimum monthly payment rate as a decimal
month = 12 

if month == 0:
    print ("Remaining balance: ", round(balance,2) )
else:
    for b in range (0, month):   # calculating balance after x months of paying only minimum monthly payments
    
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        updBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if updBalance < balance:
            balance = updBalance
            month -= 1
            print ("Month ", (b+1), " Remaining balance: ", round(balance,2) )
        


