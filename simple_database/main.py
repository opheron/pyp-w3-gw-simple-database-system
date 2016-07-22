from .config import *
import os

def create_database(db_name):
    # check if file exists:
    # if os.path.isfile(BASE_DB_FILE_PATH + db_name + '.dat'):
    #     raise DatabaseExistsErorr()
    filepath = os.path.join(BASE_DB_FILE_PATH, db_name) + ".dat"
    # Check that the path exists, create it if not
    if not os.path.exists(BASE_DB_FILE_PATH):
        os.makedirs(BASE_DB_FILE_PATH)
    # Make sure there isn't an existing DB file present then create one
    if not os.path.isfile(filepath):
        with open(filepath, "w+") as db_file:
            return Database(db_name)
    else: # We've alredy got a DB file, exit
        raise DatabaseExists()
        
    ### return Database()
# db = create_database(db_name)

def connect_database(db_name):
    raise NotImplementedError()

class Database(object):
    def __init__(self, database_name):
        self.database_name = database_name
        self.database = {}

    def create_table(self, table_name, columns):
        table = {   "name": table_name,
                    "columns": columns,
                    "data": []
        }
        
        setattr(self, table_name, table)
        
        # write var table to file
        
    def count(self, table_name):
        return len(self.table_name["data"])
        
    #db = Database("blah")
    #db.count()
    #want db.authors.count(#)
    def add_count_method(self, table_name):
        temp_table = table_name
        setattr(self.temp_table, 'count', count)

    

            # self.db.create_table('authors', columns=[
            # {'name': 'id', 'type': 'int'},
            # {'name': 'name', 'type': 'str'},
            # {'name': 'birth_date', 'type': 'date'},
            # {'name': 'nationality', 'type': 'str'},
            # {'name': 'alive', 'type': 'bool'},

        #self.db.authors.insert(1, 'Jorge Luis Borges', date(1899, 8, 24), 'ARG', False)
        #self.db.authors.insert(2, 'Edgard Alan Poe', date(1809, 1, 19), 'USA', False)