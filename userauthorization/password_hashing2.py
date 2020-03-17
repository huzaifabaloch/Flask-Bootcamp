from werkzeug.security import generate_password_hash, check_password_hash


mypasswd = 'mypasswd'
hashed_passwd = generate_password_hash(mypasswd)
print(hashed_passwd)

print(check_password_hash(hashed_passwd, mypasswd))

