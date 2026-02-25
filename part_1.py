email = input('what is your email...').strip()
username, domain = email.split('@')
if domain.endswith('.ac.uk'):
    print('Valid domain')
if '@' in email and '.' in email:
    print('Valid address')
else:
    print('invalid')