# REMEMBER - DON'T USE INSTANCE NAME AS NAME IN CONNECTION
# ALWAYS NAME INSTANCES TO INST_INSTANCENAME SO THAT I CANT GET CONFUSED
# DB ALWAYS USE db_databasename AS NAMING CONVENTIONS

from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()