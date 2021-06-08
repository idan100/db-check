import psycopg2
import os
from psycopg2 import Error

connection = ''

try:
    connection = psycopg2.connect(user=os.environ.get('USERNAME'),
                                  password=os.environ.get('PASSWORD'),
                                  host=os.environ.get('IP'),
                                  port=os.environ.get('PORT'),
                                  database=os.environ.get('DB_NAME'))

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
