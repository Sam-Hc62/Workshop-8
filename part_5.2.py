import re
ID = input('what is your ID...')
if re.search(r'^[a-zA-Z]{4}\d{4}$', ID):
    print('valid')
else:
    print('invalid')