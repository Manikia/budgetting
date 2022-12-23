from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='root', password='8162',
                           database='papiMoney')
cursor = cnx.cursor() #this is needed to be able to write to the database

DB_NAME = 'papiMoney'

TABLES = {}  #initializing an empty dictionary so we can create multiple with different keys

# TABLES['user'] = (
#     "CREATE TABLE `user` ("
#     "  `first_name` varchar(6) NOT NULL,"
#     "  `last_four_digits` int(5) NOT NULL,"
#     "  PRIMARY KEY (`first_name`)" #pk as name and card so that it knows to find that detail depending on the user
#     ") ENGINE=InnoDB")


TABLES['spending'] = (
    "UPDATE TABLE `spending` ("
    " `id` int(100) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(6) NOT NULL,"
    "  `item_name` varchar(14) NOT NULL,"
    "  `category` varchar(14) NOT NULL,"
    "  `price` float(11) NOT NULL,"
    "  PRIMARY KEY (`id`), KEY `id` (`id`)"
    # "  CONSTRAINT `spending_ibfk_1` FOREIGN KEY (`first_name`) " #the obfk1 means that its a foreignkey from spending its just a nice way of formatting
    # "     REFERENCES `user` (`first_name`) ON DELETE CASCADE" #on delete cascade means that if the foreign key ever gets deleted on the parent then it will be removed from here as well
    ") ENGINE=InnoDB")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
        
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
