from cursor import cursor, connection
from inputs import INPUT
from string import Template
import pandas as pd
from menu import Menu
from data_columns import COLUMN

class SQL_INTERFACE:


    class show_all:

        columns = COLUMN()

        def customers(self):
            connection.ping()
            CustomerTableSql = "SELECT * FROM CUSTOMER;"
            cursor.execute(CustomerTableSql)
            rows = cursor.fetchall()
            df = pd.DataFrame(
                rows, columns = self.columns.customers
            )
            print("\n", df, "\n")
            connection.commit()
            connection.close()
        

        def jobs(self):
            connection.ping()
            JobsTableSql = "SELECT * FROM JOBS;"
            cursor.execute(JobsTableSql)
            rows = cursor.fetchall()
            df = pd.DataFrame(
                rows, columns = self.columns.jobs
            )
            print("\n", df, "\n")
            connection.commit()
            connection.close()

        
        def designers(self):
            connection.ping()
            DesignerTableSql = "SELECT * FROM DESIGNER;"
            cursor.execute(DesignerTableSql)
            rows = cursor.fetchall()
            df = pd.DataFrame(
                rows, columns = self.columns.designers
            )
            print("\n", df, "\n")
            connection.commit()
            connection.close()

        
        def installers(self):
            connection.ping()
            InstallerTableSql = "SELECT * FROM INSTALLER;"
            cursor.execute(InstallerTableSql)
            rows = cursor.fetchall()
            df = pd.DataFrame(
                rows, columns = self.columns.installers
            )
            print("\n", df, "\n")
            connection.commit()
            connection.close()


    class add_new:


        def job(self):
            get = INPUT()
            L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
            CUSTOMER = L_NAME, F_NAME
            DESIGNER = get.DESIGNER_AS_FOREIGN_KEY()
            INSTALLER = get.INSTALLER_AS_FOREIGN_KEY()
            BOXES_IN = get.BOXES_IN()
            TOTAL_BOXES = get.TOTAL_BOXES()
            BLINDS_ON_HAND = get.BLINDS_ON_HAND()
            BLIND_COUNT = get.BLIND_COUNT()
            SCOPE = get.SCOPE()
            READY_TO_SCHEDULE = get.READY_TO_SCHEDULE(BOXES_IN, TOTAL_BOXES)
            JOB_ID = get.JOB_ID(L_NAME + F_NAME)
            JobsTableSql = Template('INSERT INTO JOBS \
                (JOB_ID, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE) VALUES \
                    ("$JOB_ID", "$CUSTOMER", "$DESIGNER", "$INSTALLER", "$BOXES_IN", "$TOTAL_BOXES", "$BLINDS_ON_HAND", "$BLIND_COUNT", "$SCOPE", "$READY_TO_SCHEDULE");').substitute(
                        JOB_ID = JOB_ID, 
                        CUSTOMER = CUSTOMER, 
                        DESIGNER = DESIGNER, 
                        INSTALLER = INSTALLER, 
                        BOXES_IN = BOXES_IN, 
                        TOTAL_BOXES = TOTAL_BOXES,
                        BLINDS_ON_HAND = BLINDS_ON_HAND, 
                        BLIND_COUNT = BLIND_COUNT, 
                        SCOPE = SCOPE, 
                        READY_TO_SCHEDULE = READY_TO_SCHEDULE
                        )
            connection.ping()
            cursor.execute(JobsTableSql)
            connection.commit()
            connection.close()
            return L_NAME, F_NAME, DESIGNER, JOB_ID

        
        def customer(self):
            get = INPUT()
            L_NAME, F_NAME, DESIGNER, JOB_ID = self.job()
            ADDRESS = get.ADDRESS("customer")
            EMAIL = get.EMAIL("customer")
            PHONE = get.PHONE("customer")
            AVAILABILITY = get.AVAILABILITY()
            CustomerTableSql = Template('INSERT INTO CUSTOMER \
                                (F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER, JOB_ID) VALUES \
                                    ("$F_NAME", "$L_NAME", "$ADDRESS", "$EMAIL", "$PHONE", "$AVAILABILITY", "$DESIGNER", "$JOB_ID");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME, 
                                        ADDRESS = ADDRESS, 
                                        EMAIL = EMAIL, 
                                        PHONE = PHONE, 
                                        AVAILABILITY = AVAILABILITY, 
                                        DESIGNER = DESIGNER, 
                                        JOB_ID = JOB_ID
                                        )
            connection.ping()
            cursor.execute(CustomerTableSql)
            connection.commit()
            connection.close()

        
        def designer(self):
            get = INPUT()
            L_NAME, F_NAME = get.DESIGNER_AS_FOREIGN_KEY()
            EMAIL = get.EMAIL("designer")
            PHONE = get.PHONE("designer")
            COMPANY = get.COMPANY()
            AREA = get.AREA()
            DesignerTableSql = Template('INSERT INTO DESIGNER \
                                (F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA) VALUES \
                                    ("$F_NAME", "$L_NAME", "$EMAIL", "$PHONE", "$COMPANY", "$AREA");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME,
                                        EMAIL = EMAIL,
                                        PHONE = PHONE,
                                        COMPANY = COMPANY,
                                        AREA = AREA
                                    )
            connection.ping()
            cursor.execute(DesignerTableSql)
            connection.commit()
            connection.close()

        
        def installer(self):
            get = INPUT()
            L_NAME, F_NAME = get.INSTALLER_AS_FOREIGN_KEY()
            PHONE = get.PHONE("installer")
            EMAIL = get.EMAIL("installer")
            InstallerTableSql = Template('INSERT INTO INSTALLER\
                                    (F_NAME, L_NAME, PHONE, EMAIL) VALUES \
                                    ("$F_NAME", "$L_NAME", "$PHONE", "$EMAIL");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME,
                                        PHONE = PHONE,
                                        EMAIL = EMAIL
                                    )             
            connection.ping()
            cursor.execute(InstallerTableSql)
            connection.commit()
            connection.close()

    
    class search_for:

        class customer:
            def by_name(self):
                get = INPUT()
                L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
                CustomerSearchQuery = Template('SELECT F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY FROM CUSTOMER WHERE F_NAME="$F_NAME" AND L_NAME="$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
                connection.ping()
                cursor.execute(CustomerSearchQuery)
                result = cursor.fetchone()
                print(result)
                return result


        class job:
            def by_customer_name(self):
                get = INPUT()
                CUSTOMER = get.CUSTOMER_AS_FOREIGN_KEY()
                JobSearchQuery = Template('SELECT JOB_ID, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOBS WHERE CUSTOMER = "$CUSTOMER";').substitute(
                    CUSTOMER = CUSTOMER
                )
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchone()
                print(result)
                return result
            
            def by_ready_to_schedule(self):
                JobSearchQuery = 'SELECT CUSTOMER FROM JOBS WHERE READY_TO_SCHEDULE = 1;'
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchmany()
                for row in result:
                    print(row)
        

        class designer:
            def by_name(self):
                get = INPUT()
                L_NAME, F_NAME = get.DESIGNER_AS_FOREIGN_KEY()
                DesignerSearchQuery = Template('SELECT F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA FROM DESIGNER WHERE F_NAME = "$F_NAME" and L_NAME = "$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
                connection.ping()
                cursor.execute(DesignerSearchQuery)
                result = cursor.fetchone()
                print(result)
                return result
    

    class update:
        class job:
            def blind_and_box_count(self):
                """ PATTERN: Grab BOX_COUNT, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT
                             Display all gathered columns
                             Update count
                             Determine if Ready to schedule
                """
                get = INPUT()
                L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
                _hash = get.JOB_ID(L_NAME + F_NAME)
                query = Template('SELECT CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT FROM JOBS WHERE JOB_ID = "$_hash";').substitute(_hash = _hash)
                connection.ping()
                cursor.execute(query)
                result = cursor.fetchone()
                CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT = result
                df = pd.DataFrame(
                    {
                        "CUSTOMER": [CUSTOMER],
                        "BOXES IN WAREHOUSE": [BOXES_IN],
                        "BOXES NEEDED" : [TOTAL_BOXES],
                        "BLINDS IN WAREHOUSE": [BLINDS_ON_HAND],
                        "BLINDS NEEDED" : [BLIND_COUNT]
                    }
                )
                print("\n", df, "\n")
                count_menu = Menu()
                option = -1
                while option != 2:
                    option = count_menu.update_blind_and_box_count()
                    if option == 0:
                        BOXES_IN = BOXES_IN + get.NEW_NUMBER("boxes")
                    elif option == 1:
                        BLINDS_ON_HAND = BLINDS_ON_HAND + get.NEW_NUMBER("blinds")
                    else:
                        continue
                READY_TO_SCHEDULE = get.READY_TO_SCHEDULE(BOXES_IN, TOTAL_BOXES)
                query = Template('UPDATE JOBS SET BOXES_IN = "$BOXES_IN",\
                                                  BLINDS_ON_HAND="$BLINDS_ON_HAND",\
                                                  READY_TO_SCHEDULE="$READY_TO_SCHEDULE" \
                                                  WHERE JOB_ID = "$_hash";').substitute(
                                                      BOXES_IN = BOXES_IN,
                                                      BLINDS_ON_HAND = BLINDS_ON_HAND,
                                                      READY_TO_SCHEDULE = READY_TO_SCHEDULE,
                                                      _hash = _hash
                                                  )
                connection.ping()
                cursor.execute(query)
                connection.commit()
                connection.close()
                query = Template('SELECT CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT FROM JOBS WHERE JOB_ID = "$_hash";').substitute(_hash = _hash)
                connection.ping()
                cursor.execute(query)
                result = cursor.fetchone()
                CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT = result

                SCHEDULE = -1
                if READY_TO_SCHEDULE == 1:
                    SCHEDULE = True
                else:
                    SCHEDULE = False

                df = pd.DataFrame(
                    {
                        "CUSTOMER": [CUSTOMER],
                        "BOXES IN WAREHOUSE": [BOXES_IN],
                        "BOXES NEEDED" : [TOTAL_BOXES],
                        "BLINDS IN WAREHOUSE": [BLINDS_ON_HAND],
                        "BLINDS NEEDED" : [BLIND_COUNT],
                        "READY TO SCHEDULE" : [SCHEDULE]
                    }
                )
                print("\n\t\t[UPDATED JOB]\n\n", df, "\n")






