from basic import db, Puppy


# Creates all the python Models --> DB Table
db.create_all()

tuna = Puppy('Tuna', 9)
toast = Puppy('Toaster', 14)

# None
# None
print(tuna.id)
print(toast.id)

# Adding all objects to the database.
db.session.add_all([tuna, toast])
db.session.commit()

print(tuna.id)
print(toast.id)