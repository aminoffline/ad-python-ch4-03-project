import mysql.connector
from mysql.connector import errorcode

#DataBase_name = input('Name of DataBase: ')
DataBase_name = 'truecar'

config ={
    'user':'Amin',
    'password':'Adv@ncePyth0n',
    'host':'localhost',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def Create_database(name):
    sql = f'CREATE DATABASE IF NOT EXISTS {name}'
    cursor.execute(sql)

Tables = {}

Tables['cars'] = (
    "CREATE TABLE IF NOT EXISTS `cars` ("
    " `id` SMALLINT NOT NULL AUTO_INCREMENT,"
    " `vehicle_title` VARCHAR (200) NOT NULL,"
    " `vehicle_mileage` VARCHAR (100),"
    " `vehicle_color` VARCHAR (150),"
    " `vehicle_condition` VARCHAR (200),"
    " `vehicle_location` VARCHAR (200),"
    " `vehicle_price` VARCHAR (50),"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

def Create_Tables(Tables):
    cursor.execute(f'USE {DataBase_name}')
    for i in Tables:
        table = Tables[i]
        try:
            print(f"Creating table {i}")
            cursor.execute(table)
        except mysql.connector.Error as err:
            if err == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exist")
            else:
                print(err.msg)

Create_database(DataBase_name)
Create_Tables(Tables)