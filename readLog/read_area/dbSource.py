__author__ = 'Colin1'

import umysql

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_DB = 'tuan'
cnn = umysql.Connection()


def mysql_connect():
    cnn.connect(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DB)

def mysql_query(sql):
    return cnn.query(sql)

def mysql_close():
    cnn.close()