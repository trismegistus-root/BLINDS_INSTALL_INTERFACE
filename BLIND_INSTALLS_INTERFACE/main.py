from sql_interface import SQL_INTERFACE
from driver import driver

if __name__ == "__main__":
    database = SQL_INTERFACE()
    driver(database)