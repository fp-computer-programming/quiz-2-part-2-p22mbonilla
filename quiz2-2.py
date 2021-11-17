# Author MB 11/17/2021

st = input('give me how you are feeling: ')
st = str(st)
if st == 'happy':
    st = 'not' + ' ' + st
else:
    st = st

print('you are' + ' ' + st + ', ' + 'now SCRAM')
