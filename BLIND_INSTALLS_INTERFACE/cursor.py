import pymysql as sql
connection = sql.connect(host="localhost", user="root",passwd="", database="BLIND_INSTALLS")
cursor = connection.cursor()

