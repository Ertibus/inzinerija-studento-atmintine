import sqlite3
import sys
import os

# Database class for instancing a connection to a database. Should be created by a repository class
class Database:
    __db = None

    def __init__(self, location: str):
        self.start_connection(location)

    def start_connection(self, location: str):
        try:
            self.__db = sqlite3.connect(location, check_same_thread=False)
        except Exception as e:
            print(f'{e}')
            sys.exit(1)

    def stop_connection(self):
        self.__db.close()

    def get_cursor(self):
        return self.__db.cursor()

    def commit(self):
        self.__db.commit()

# Don't use this class by itself. Create a new class and inherit it!
class Repository():
    # Private database object
    __db = None
    # Private database cursor for query execution
    __db_cursor = None

    # Establish connection with the database by instancing a new database object. If object does not exits - creates a new database
    @classmethod
    def connect(cls, database_path: str):
        # Only establish a connection is one is not already created
        if cls.__db == None:
            if not os.path.exists(database_path):
                cls.__db = Database(database_path);
                cls.__db_cursor = cls.__db.get_cursor()
                cls.__db_cursor.execute(' CREATE TABLE IF NOT EXISTS "Event" ("title"	TEXT NOT NULL, "description"	TEXT, "deadline"	TEXT NOT NULL, "id"	INTEGER NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT)); ')
                cls.__db_cursor.execute('CREATE TABLE IF NOT EXISTS "User" ("username"	TEXT NOT NULL UNIQUE, "password"	TEXT NOT NULL, "question_id" ITEGER NOT NULL, "answer" TEXT NOT NULL);')
            else:
                cls.__db = Database(database_path);
                cls.__db_cursor = cls.__db.get_cursor()

    # Return a single value. Possible returns: 1 or "string"
    @classmethod
    def get_value(cls, sql_query: str):
        cls.__db_cursor.execute(sql_query)
        for x in cls.__db_cursor:
            return x[0]
        return None

    # Return multiple results as a list. Possible returns: [1, 2, 3] or ['string', 'str', 'String'] or [['id', 'string', 1] or ['id','string', 2]]
    @classmethod
    def get_list(cls, sql_query: str, parameters = {}):
        if cls.__db is None or cls.__db_cursor is None:
            cls.connect()

        cls.__db_cursor.execute(sql_query, parameters)

        ret_list: list = []
        for x in cls.__db_cursor:
            ret_list.append(x)

        return ret_list
    
    

    # Create, Delete or Update query executor
    @classmethod
    def commit_query(cls, sql_query, parameters):
        if cls.__db is None or cls.__db_cursor is None:
            cls.connect()

        cls.__db_cursor.execute(sql_query, parameters)
        cls.__db.commit()


    """
    ---------
    Example
    ---------
    from program.repo.database import Repository

    class NewRepository(Repository)
        @classmethod
        def get_quary_results(cls, value: str):
            if not value or value.isspace():
                raise ValueError("Bad value given for query search")

            ret = cls.get_value("SELECT `value` FROM table WHERE arg = 1")
            # or
            ret = cls.get_list("SELECT `:value` FROM :table WHERE arg = :arg", {
                "value": value,
                "table": "table",
                "arg": 1,
            })

            if not ret:
                raise ValueError("Not found")
            return ret
    """
