import pymysql as sql
connection = sql.connect(host="localhost", user="root",passwd="", database="BLIND_INSTALLS")
cursor = connection.cursor()

"""
InstallerTableSql = "SELECT * FROM INSTALLER;"
cursor.execute(InstallerTableSql)
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()
"""