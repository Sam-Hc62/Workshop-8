import re
email = input('what is your email...').strip()
if re.search('.+@.+', email):
    print('valid')