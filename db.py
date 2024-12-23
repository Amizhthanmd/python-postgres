import psycopg2
from psycopg2 import sql

class InitDb():
    def create_database_if_not_exists(db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
            connection.autocommit = True
            cursor = connection.cursor()

            # Check if database exists
            cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [db_name])
            if not cursor.fetchone():
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))

            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error creating database: {e}")
