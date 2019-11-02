# [2019-08-05] Challenge #380 [Easy] Smoshed Morse Code 1


import string

# Entering all the codes in alphabetical order

morseCodeGuide = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split ()
alpha = string.ascii_lowercase  # Gets the alphabets as a list
joiner = dict ( zip ( alpha, morseCodeGuide ) )  # Joins the two list as a dictionary



def encrypter(input) :
    return ' '.join ( joiner[i] for i in input.lower () )


# Test
assert (encrypter ( 'sos' )) == '... --- ...'  # Testing

# input
inp = input ( "Enter a string" )
print ( encrypter ( inp ) )
