#!/usr/bin/python3
"""Generate token that expires."""
from datetime import datetime, timedelta
from random import randint
from time import sleep

# Dictionary to store tokens and their expiration dates
tokens = {}

def generate_token():
    """Generate a token."""
    token = str(randint(100000, 999999))

    # Set token expiration 1 minute from the current time
    expiration_time = datetime.now() + timedelta(minutes=1)
    tokens[token] = expiration_time
    print(f"Generated token: {token} (expires at {expiration_time})")
    return token

def is_token_valid(token):
    """Check the validity of a token and delete it if it's expired."""
    current_time = datetime.now()
    if token in tokens:
        if current_time > tokens[token]:
            del tokens[token]
            print(f"Token {token} has expired and is deleted")
            return False
        else:
            print(f"Token {token} is still valid until {tokens[token]}")
            return True
    print(f"Token {token} does not exist")
    return False

def count_down(minutes):
    """Count down from 1 to the specified number of minutes."""
    for minute in range(1, minutes + 1):
        print(f"{minute} minute(s) remaining...")
        sleep(60)  # Delay for 60 seconds

if __name__ == '__main__':
    token = generate_token()

    is_token_valid(token)

    # Simulate waiting for the token to expire
    count_down(2)  # Wait for 2 minutes

    # Check the token after waiting
    is_token_valid(token)
