from sql_interface import SQL_INTERFACE
from driver import driver

if __name__ == "__main__":
    db = SQL_INTERFACE()
    driver(db)