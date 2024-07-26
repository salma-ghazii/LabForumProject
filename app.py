import database

# Just messing around to make sure the database works
database.connect_db()
database.create_tables()
# database.insert_lab("Newark, NJ")
print(database.get_labs())
database.delete_lab(1)
print(database.get_labs())
