import pytest

def extract_username(emails):
    return [email.split('@')[0] for email in emails]

def test_extract_username():
    emails = ['test@example.com', 'user@example.org', 'admin@example.net']
    expected_usernames = ['test', 'user', 'admin']
    assert extract_username(emails) == expected_usernames

def test_extract_username_empty_list():
    emails = []
    expected_usernames = []
    assert extract_username(emails) == expected_usernames

def test_extract_username_single_email():
    emails = ['test@example.com']
    expected_usernames = ['test']
    assert extract_username(emails) == expected_usernames

def test_extract_username_invalid_email():
    emails = ['invalid_email']
    with pytest.raises(IndexError):
        extract_username(emails)
