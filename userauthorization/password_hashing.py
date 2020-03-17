from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

passwd = 'supersecretpassword'

# Generating password hash
hashed_passwd = bcrypt.generate_password_hash(password=passwd)

print(hashed_passwd)

# Check Password 
check = bcrypt.check_password_hash(hashed_passwd, passwd)

print(check)