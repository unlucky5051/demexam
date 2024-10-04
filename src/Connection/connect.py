from peewee import *
from pymysql import *
mysql_db = MySQLDatabase('ZHuV1234_demoexam',
                         user = 'ZHuV1234_VV',
                         password='dadrip08115',
                         host = '10.11.13.118',
                         port=3306)

if __name__ == "__main__":
    print(mysql_db.connect())