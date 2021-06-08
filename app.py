import psycopg2
from psycopg2 import Error

connection = ''

try:
    connection = psycopg2.connect(user=input('username:'),
                                  password=input('password:'),
                                  host=input('ip:'),
                                  port=input('port:'),
                                  database=input('db name:'))

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Connected successfully!")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:")
    print(error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
