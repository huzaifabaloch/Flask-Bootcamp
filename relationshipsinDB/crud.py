from model import db, Puppy, Toy, Owner


# Creating two puppies
rufus = Puppy('Rufus')
tuna = Puppy('Tuna')

# Add puppies to the DB
db.session.add_all([rufus, tuna])
db.session.commit()

all_pups = Puppy.query.all()
print(all_pups)


tuna = Puppy.query.filter_by(name='Tuna').first()
print(tuna)


# Create Owner object
huzaifa = Owner('Huzaifa', tuna.id)

# Giving toys to Tuna
toy1 = Toy('Chew Toy', tuna.id)
toy2 = Toy('Ball', tuna.id)
toy3 = Toy('Roblox', tuna.id)

db.session.add_all([huzaifa, toy1, toy2, toy3])
db.session.commit()


# Grab Tuna again
tuna = Puppy.query.filter_by(name='Tuna').first()
print(tuna)


# ALL TOYS
tuna.report_toys()