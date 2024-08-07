users = [
    {'id': 1, 'username': 'Bret'},
    {'id': 2, 'username': 'Antonette'},
    {'id': 3, 'username': 'Samantha'}
]

user_lookup = {user['id']: user['username'] for user in users}
print(user_lookup)

