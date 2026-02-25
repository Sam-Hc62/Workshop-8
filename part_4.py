import re
email = input('what is your email...').strip()
if re.search(r'^.+\w@\w.+\.(ac.uk | gov.uk | nhs.net)$', email):
    print('valid')