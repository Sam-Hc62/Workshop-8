import re
email = input('what is your email...').strip()
if re.search(r'^.+[a-zA-Z0-9_]@[a-zA-Z0-9_].+\.ac.uk$', email):
    print('valid')