import uuid

# Generate a UUID and extract a 5-digit portion
confirmation_token = int(str(uuid.uuid4().int)[:5])

print(confirmation_token)
