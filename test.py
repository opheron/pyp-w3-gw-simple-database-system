from simple_database import *

mydb = Database("test_database")
mydb.create_table('authors', columns=[
            {'name': 'id', 'type': 'int'},
            {'name': 'name', 'type': 'str'},
            {'name': 'birth_date', 'type': 'date'},
            {'name': 'nationality', 'type': 'str'},
            {'name': 'alive', 'type': 'bool'},
        ])
#print(mydb.authors)
print(mydb.authors.count())
