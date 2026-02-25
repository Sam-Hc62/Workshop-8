from validator import is_valid_email

def test_valid_emails():
    assert is_valid_email("student1@kent.ac.uk") == True
    assert is_valid_email("doctor@nhs.net") == True