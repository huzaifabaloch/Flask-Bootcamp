from basic import db, Puppy


# CREATE NEW Object.
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

# READ 
# ALL_PUPPIES
all_puppies = Puppy.query.all()  # list of puppies objects in table.
print(all_puppies)

# SELECT OR READ BY ID.
puppy_one = Puppy.query.get(1)
print(puppy_one)

# FILTERS
# Produce some SQL code
puppy_toast = Puppy.query.filter_by(name='Toaster')
print(puppy_toast.all())

# UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# DELETE
second = Puppy.query.get(2)
db.session.delete(second)
db.session.commit()


all_puppies = Puppy.query.all()
print(all_puppies)