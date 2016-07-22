from .config import *
from .exceptions import *
import os
import pickle

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
            my_db = Database(db_name, filepath)
            pickle.dump(my_db, db_file)
            return Database(db_name, filepath)
    else: # We've alredy got a DB file, exit
        raise ValidationError('Database with name "' + db_name + '" already exists.')
        
    ### return Database()
# db = create_database(db_name)

def connect_database(db_name):
    filepath = os.path.join(BASE_DB_FILE_PATH, db_name) + ".dat"
    with open(filepath, "r+") as db_file: 
        db = pickle.load(db_file)
        return db

class Database(object):
    def __init__(self, database_name, filepath):
        self.database_name = database_name
        self.filepath = filepath
        self.table_list = []
    

        
        
    # def count(self, table_name):
    #     return len(self.table_name["data"])
    
    def show_tables(self):
        return self.table_list
        
                                        
    def create_table(self, table_name, columns):
        setattr(self, table_name, Table(table_name, columns, self))
        self.table_list.append(table_name)
        
        # write var table to file
        
class Table(object):
    
    def __init__(self, name, columns, db_object):
        self.name = name
        self.db_object = db_object
        self.columns= columns
        self.data = []
    
    def count(self):
        return len(self.data)

    def insert(self, *args):
        if len(args) != len(self.columns):
            raise ValidationError('Invalid amount of field')
        else:    
            self.data.append(list(args))
            filepath = self.db_object.filepath
            with open(filepath, "r+") as db_file:
                pickle.dump(self.db_object, db_file)
        
    def describe(self):
        return self.columns
        
    # def all(self):
    #     for datum in self.data:
    #         yield datum
        
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