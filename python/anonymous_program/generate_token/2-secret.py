import secrets

# Generate a 5-digit random number
confirmation_token = secrets.randbelow(90000) + 10000

print(confirmation_token)
