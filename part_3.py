import re
email = input('what is your email...').strip()
if re.search(r'^.+[^@]@[^@].+\.ac.uk$', email):
    print('valid')