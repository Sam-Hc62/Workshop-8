import re
import csv
def is_valid_email(email):
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|nhs.net)$", email):
        return True
    return False
def main():
    email = input("What's your email? ").strip()
    name = input('what is your name...')
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")
if __name__ == "__main__":
    main()