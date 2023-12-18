from sql_queries import create_table_queries
import psycopg2


def connection():
    """
        This function enables connection between Python and my Postgres DB
    """
    connector = psycopg2.connect(
        database = "Music",
        host = "127.0.0.1",
        user = "postgres",
        password = "@SSitanecl94"
    )
    cursor = connector.cursor()

    return cursor, connector

def hello_test():
    print("toto")


def create_tables(cursor, connector):
    """
        This function executes the queries and commit the changes into my DB
    """
    for query in create_table_queries:
        cursor.execute(query)
        connector.commit()


def main():
    """
        Main function
    """
    cur, conn = connection()
    print("Connection to the db establised successfull!")
    
    # create_tables(cur, conn)
    # print("Tables created successfull!")
    
    cur.close()

