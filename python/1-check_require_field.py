required_field = ['name', 'email', 'password']
data = {'name': 'wisdom', 'email': 'test@gmail.com', 'password': '12345'}

for field in required_field:
    if not data.get(field):
        print(f"{field} is require")
