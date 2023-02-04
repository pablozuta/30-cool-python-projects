'''
This is an interesting Python project that uses the secrets and string modules to generate a strong and secure password, much like you can with popular password managers.
The string module obtains all possible letters, digits, and special characters, while the secrets module allows us to obtain cryptographically secure passwords.
The code for this project is relatively simple as it uses a loop to continually generate passwords until it contains at least one special character and two digits. 
'''
import secrets
import string

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
                pw_strong = True  

              

    return pwd



if __name__ == '__main__':
   print(create_pw())