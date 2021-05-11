# REMEMBER - DON'T USE INSTANCE NAME AS NAME IN CONNECTION
# ALWAYS NAME INSTANCES TO INST_INSTANCENAME SO THAT I CANT GET CONFUSED
# DB ALWAYS USE db_databasename AS NAMING CONVENTIONS

# from app import db, Users

# db.drop_all()
# db.create_all()

# testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
# db.session.add(testuser)
# db.session.commit()

#from app import db, Countries, Cities
from app import db, Orders, Products#, ChosenItems

db.drop_all()
db.create_all() # Creates all table classes defined

# UK = Countries(name = 'United Kingdom')
# db.session.add(UK)
# db.session.commit()

# ldn = Cities(name='London', country = UK)
# mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

# db.session.add(ldn)
# db.session.add(mcr)
# db.session.commit()