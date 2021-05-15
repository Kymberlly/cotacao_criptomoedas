from mysql.connector import connect, Error
from os import environ

try:
    with connect(host=environ['HOST'], user=environ['USER'], password=environ['PASSWORD']) as connection:
        print(connection)
except Error as e:
    print(e)
