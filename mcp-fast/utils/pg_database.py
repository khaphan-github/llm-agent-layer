import psycopg2
from psycopg2.extras import execute_values
class PGDatabase:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print(self.connection.get_dsn_parameters(), "\n")

            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error executing query", error)
            return None
    def execute_query_many(self, query, params_list):
        try:
            # Ensure the query has RETURNING id
            self.cursor.execute("BEGIN;")  # Start a transaction
            execute_values(self.cursor, query, params_list)
            
            # Fetch all returned IDs
            inserted_ids = [row[0] for row in self.cursor.fetchall()]
            
            self.connection.commit()
            return inserted_ids  # Return list of inserted IDs
        except (Exception, psycopg2.Error) as error:
            print("Error executing multiple queries", error)
            self.connection.rollback()
            return None  # Indicate failure
        
    def begin_transaction(self):
        try:
            self.cursor.execute("BEGIN;")
        except (Exception, psycopg2.Error) as error:
            print("Error beginning transaction", error)

    def commit_transaction(self):
        try:
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error committing transaction", error)

    def rollback_transaction(self):
        try:
            self.connection.rollback()
        except (Exception, psycopg2.Error) as error:
            print("Error rolling back transaction", error)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


