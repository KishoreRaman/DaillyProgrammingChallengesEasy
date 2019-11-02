# [2019-07-15] Challenge #379 [Easy] Progressive taxation


# Tax rate calculator
bracket1 = 10000
bracket2 = 30000
bracket3 = 100000


def calculcator(income) :
    tax = 0
    income = (int ( income ))
    if (income > bracket3) :
        tax = .4 * (income - 100000)
        income = bracket3
    if (income > bracket2) :
        tax = (income - bracket2) * .25 + tax
    income = bracket2
    if (income > bracket1) :
        tax = (income - bracket1) * .1 + tax
    income = income - bracket1
    overAllTaxRate = (int ( tax ) / income)
    return int ( tax ), overAllTaxRate * 100


income = input ( "Enter your income: " )
tax = (calculcator ( income )[0])
rate = (calculcator ( int ( income ) )[1])
print ( 'Tax to be paid : {0}\n Overall Tax Rate : {1:.2f}%'.format ( tax, rate ) )
