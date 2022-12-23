#function that gets data from api: name, category, price, and product name
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

value = input("Insert name, product name, category, and price in order: \n")
(name, product, category, price) = value.split(' ')

print(name)
print(product)
print(category)
print(price)

print('\nAdding to database\n')

def creatingData(name, product, category, price):
    cnx = mysql.connector.connect(user='root', password='8162',
                            database='papiMoney')
    cursor = cnx.cursor()

    date_added = datetime.now().date()
    
    
    add_spending = ("INSERT INTO spending "
                "(date_added, first_name, item_name, category, price) "
                "VALUES (%(date_added)s, %(first_name)s, %(item_name)s, %(category)s, %(price)s)")
    
    data_spending = {
    'date_added': date_added,
    'first_name':name,
    'item_name':product,
    'category':category,
    'price':price,
    } #we would try to manipulate so that the api inserts this data
    cursor.execute(add_spending, data_spending)
    
    # Make sure data is committed to the database
    id = cursor.lastrowid
    cursor.close()
    cnx.commit()
    cnx.close()

creatingData(name, product, category, price)

#in the database decimal works if we dont have the above in a method but float wont work and it will timeout but if we set it as a method, float will work and decimal wont and give us a timeout error