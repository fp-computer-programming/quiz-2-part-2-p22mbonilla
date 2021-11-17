# Author MB 11/17/2021

let = input(str('what letter is it A-G: '))

if let == 'A':
    let = 'a'
elif let == 'C':
    let = 'c'
elif let == 'E':
    let = 'e'
else:
    let = 'whatever'

if let == 'a':
    print('You have class today because it is A day.')
elif let == 'c':
    print('You have class today because it is C day.')
elif let == 'e':
    print('You have class today because it is E day.')
else:
    print('You don\'t have class today')
