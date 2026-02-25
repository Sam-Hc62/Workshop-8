email = input('what is your email...').strip()

if '@' in email and '.' in email:
    print('Valid')
else:
    print('invalid')