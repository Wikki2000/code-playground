#!/usr/bin/python3
"""Generate token that expires."""
from redis import Redis
import secrets
from datetime import timedelta
import time

# Connect to redis
r = Redis(host='localhost', port=6379, db=0)

def generate_token():
    """Generate a 5-digit random number."""
    token = str(secrets.randbelow(90000) + 10000)
    expiration_time = timedelta(seconds=3)
    r.setex(token, expiration_time, 'valid')
    return token

def is_token_valid(token):
    """Check if token exists."""
    return r.exists(token)

# Generate a token
token = generate_token()
print(f"Generated token: {token}")

# Check if the token is valid (within 3 minutes)
print(f"Is token valid? {is_token_valid(token)}")

# Simulate waiting for the token to expire
time.sleep(4)  # Wait for 4 minutes

# Check if the token is valid (after 3 minutes)
print(f"Is token valid? {is_token_valid(token)}")
