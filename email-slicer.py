email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} and the domain is {domain}")