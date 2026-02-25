import re
number = input('what is your phone number...')
if re.search(r'^07\d{9}$', number):
    print('valid')
else:
    print('invalid')