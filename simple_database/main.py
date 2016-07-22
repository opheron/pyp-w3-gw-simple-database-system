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
        #self.database = {}
        self.table_list = []
        
        
    # def count(self, table_name):
    #     return len(self.table_name["data"])
    
    def show_tables(self):
        return self.table_list
        
                                        
    def create_table(self, table_name, columns):
        setattr(self, table_name, Table(table_name, columns))
        self.table_list.append(table_name)
        
        # write var table to file
        
class Table(object):
    
    def __init__(self, name, columns):
        self.name = name
        self.columns= columns
        self.data = []
    
    def count(self):
        return len(self.data)

    def insert(self, *args):
        self.data.append(list(args))
        
    #db = Database("blah")
    #db.count()
    #want db.authors.count(#)


            # self.db.create_table('authors', columns=[
            # {'name': 'id', 'type': 'int'},
            # {'name': 'name', 'type': 'str'},
            # {'name': 'birth_date', 'type': 'date'},
            # {'name': 'nationality', 'type': 'str'},
            # {'name': 'alive', 'type': 'bool'},

        #self.db.authors.insert(1, 'Jorge Luis Borges', date(1899, 8, 24), 'ARG', False)
        #self.db.authors.insert(2, 'Edgard Alan Poe', date(1809, 1, 19), 'USA', False)