import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='ming', password='', database='cqavoting')

cursor = mariadb_connection.cursor()

mariadb_connection.close()

