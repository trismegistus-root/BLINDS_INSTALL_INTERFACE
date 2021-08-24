from cursor import cursor, connection
from inputs import INPUT
from string import Template
import pandas as pd
from menu import Menu
from data_columns import COLUMN
from alert_colors import colors


class SQL_INTERFACE:


    class show_all:

        columns = COLUMN()

        def customers(self):
            get = INPUT()
            connection.ping()
            CustomerTableSql = "SELECT F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER FROM CUSTOMER;"
            cursor.execute(CustomerTableSql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, self.columns._customer_without_jobID)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()
        

        def jobs(self):
            get = INPUT()
            connection.ping()
            JobTableSql = "SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB;"
            cursor.execute(JobTableSql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, self.columns._job_without_jobID)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()

        
        def designers(self):
            get = INPUT()
            connection.ping()
            DesignerTableSql = "SELECT * FROM DESIGNER;"
            cursor.execute(DesignerTableSql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, self.columns._designers)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()

        
        def installers(self):
            get = INPUT()
            connection.ping()
            InstallerTableSql = "SELECT * FROM INSTALLER;"
            cursor.execute(InstallerTableSql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, self.columns._installers)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()
        


    class add_new:

        def job(self):
            get = INPUT()
            L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
            CUSTOMER = L_NAME, F_NAME
            DESIGNER = get.DESIGNER_AS_FOREIGN_KEY()
            INSTALLER = get.INSTALLER_AS_FOREIGN_KEY()
            PAYS = get.PAYS()
            BOXES_IN = get.BOXES_IN()
            TOTAL_BOXES = get.TOTAL_BOXES()
            BLINDS_ON_HAND = get.BLINDS_ON_HAND()
            BLIND_COUNT = get.BLIND_COUNT()
            SCOPE = get.SCOPE()
            READY_TO_SCHEDULE = get.READY_TO_SCHEDULE(BOXES_IN, TOTAL_BOXES)
            JOB_ID = get.JOB_ID(L_NAME + F_NAME)
            JobTableSql = Template('INSERT INTO JOB \
                (JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE) VALUES \
                    ("$JOB_ID", "$PAYS", "$CUSTOMER", "$DESIGNER", "$INSTALLER", "$BOXES_IN", "$TOTAL_BOXES", "$BLINDS_ON_HAND", "$BLIND_COUNT", "$SCOPE", "$READY_TO_SCHEDULE");').substitute(
                        JOB_ID = JOB_ID, 
                        PAYS = PAYS,
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
            cursor.execute(JobTableSql)
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
            """ STILL UNDER TEST FOR InstallerPayTableQuery
            """
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
            InstallerPayTableQuery = Template('INSERT INTO INSTALLER_PAY (INSTALLER, PAY) VALUES ("$INSTALLER", "$PAY");').substitute(
                INSTALLER = (L_NAME, F_NAME),
                PAY = 0.0
            )
            connection.ping()
            cursor.execute(InstallerTableSql)
            cursor.execute(InstallerPayTableQuery)
            connection.commit()
            connection.close()

    
    class search_for:

        class customer:
            columns = COLUMN()
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
                table = get.PANDAS_TABULATED_DATAFRAME(result, self.columns._customers)
                get.and_print().COLORIZED_TABLE(table)
                return result


        class job:
            columns = COLUMN()

            def by_customer_name(self):
                get = INPUT()
                CUSTOMER = get.CUSTOMER_AS_FOREIGN_KEY()
                JobSearchQuery = Template('SELECT CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE CUSTOMER = "$CUSTOMER";').substitute(
                    CUSTOMER = CUSTOMER
                )
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, self.columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
                return result
            
            def by_ready_to_schedule(self):
                get = INPUT()
                JobSearchQuery = "SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE READY_TO_SCHEDULE = 1;"
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchall()
                table = get.PANDAS_TABULATED_DATAFRAME(result, self.columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
            
            def by_installer(self):
                get = INPUT()
                connection.ping()
                installer = get.INSTALLER_AS_FOREIGN_KEY()
                JobTableSql = Template('SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE INSTALLER = "$installer";').substitute(
                    installer = installer
                )
                cursor.execute(JobTableSql)
                rows = cursor.fetchall()
                table = get.PANDAS_TABULATED_DATAFRAME(rows, self.columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
                connection.commit()
                connection.close()
        

        class designer:
            columns = COLUMN()
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
                table = get.PANDAS_TABULATED_DATAFRAME(result, self.columns._designers)
                get.and_print().COLORIZED_TABLE(table)
                return result
        
        class installer:
            columns = COLUMN()
            def by_name(self):
                get = INPUT()
                L_NAME, F_NAME = get.INSTALLER_AS_FOREIGN_KEY()
                InstallerSearchQuery = Template('SELECT * FROM INSTALLER WHERE F_NAME="$F_NAME" AND L_NAME="$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
                connection.ping()
                cursor.execute(InstallerSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, self.columns._installers)
                get.and_print().COLORIZED_TABLE(table)
                return result
    

    class update:
        class job:
            def blind_and_box_count(self):
                """ PATTERN: Grab BOX_COUNT, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT
                             Display all gathered columns
                             Update count with INPUT() logic
                             Determine if Ready to schedule
                """
                get = INPUT()
                L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
                _hash = get.JOB_ID(L_NAME + F_NAME)
                query = Template('SELECT CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT FROM JOB WHERE JOB_ID = "$_hash";').substitute(_hash = _hash)
                connection.ping()
                cursor.execute(query)
                result = cursor.fetchone()
                CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT = result
                df_dict = {
                        "CUSTOMER": [CUSTOMER],
                        "BOXES IN WAREHOUSE": [BOXES_IN],
                        "BOXES NEEDED" : [TOTAL_BOXES],
                        "BLINDS IN WAREHOUSE": [BLINDS_ON_HAND],
                        "BLINDS NEEDED" : [BLIND_COUNT]
                    }
                df = pd.DataFrame(df_dict)
                table = get.TABULATE_UNIQUE_QUERY(df, df_dict.keys())
                get.and_print().COLORIZED_TABLE(table)
                count_menu = Menu()
                option = -1
                while option != 2:
                    option = count_menu.JOB_MENUS().update_blind_and_box_count()
                    if option == 0:
                        BOXES_IN = BOXES_IN + get.NEW_NUMBER("boxes")
                    elif option == 1:
                        BLINDS_ON_HAND = BLINDS_ON_HAND + get.NEW_NUMBER("blinds")
                    else:
                        continue
                READY_TO_SCHEDULE = get.READY_TO_SCHEDULE(BOXES_IN, TOTAL_BOXES)
                query = Template('UPDATE JOB SET BOXES_IN = "$BOXES_IN",\
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
                query = Template('SELECT CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT FROM JOB WHERE JOB_ID = "$_hash";').substitute(_hash = _hash)
                connection.ping()
                cursor.execute(query)
                result = cursor.fetchone()
                CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT = result

                SCHEDULE = -1
                if READY_TO_SCHEDULE == 1:
                    SCHEDULE = True
                    print("\n", f"{colors.TABLE}THIS JOB IS READY TO SCHEDULE{colors.ENDC}\n")
                else:
                    SCHEDULE = False
                updated_df_dict = {
                        "CUSTOMER": [CUSTOMER],
                        "BOXES IN WAREHOUSE": [BOXES_IN],
                        "BOXES NEEDED" : [TOTAL_BOXES],
                        "BLINDS IN WAREHOUSE": [BLINDS_ON_HAND],
                        "BLINDS NEEDED" : [BLIND_COUNT],
                        "READY TO SCHEDULE" : [SCHEDULE]
                    }
                df = pd.DataFrame(updated_df_dict)
                table = get.TABULATE_UNIQUE_QUERY(df, updated_df_dict.keys())
                get.and_print().COLORIZED_TABLE(table)


    class delete:

        def job(self):
            get = INPUT()
            L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
            _hash = get.JOB_ID(L_NAME + F_NAME)
            # Matt, Kaleb, Judd
            """ 1. Grab PAYS, pass to Installer under pay_table
                2. Update customer JOB_ID to NIL
                3. Remove JOB
            """
            JobPayQuery = Template('SELECT PAYS, INSTALLER FROM JOB WHERE JOB_ID = "$_hash";').substitute(
                _hash = _hash
            )
            # Treble damages - 
            UpdateCustomerJobIDQuery = Template('UPDATE CUSTOMER SET JOB_ID = "COMPLETE" WHERE F_NAME = "$F_NAME" AND L_NAME = "$L_NAME";').substitute(
                F_NAME = F_NAME,
                L_NAME = L_NAME
            )
            DeleteJobQuery = Template('DELETE FROM JOB WHERE JOB_ID = "$_hash";').substitute(
                _hash = _hash
            )
            connection.ping()
            cursor.execute(JobPayQuery)
            result = cursor.fetchone()
            connection.commit()

            getInstallerCurrentPay = Template('SELECT PAY FROM INSTALLER_PAY WHERE INSTALLER = "$INSTALLER";').substitute(
                INSTALLER = result[1]
            )
            cursor.execute(getInstallerCurrentPay)
            installer_current_pay = cursor.fetchone()
            connection.commit()
            installer_current_pay = installer_current_pay[0] + float(result[0])
            UpdateInstallerPayQuery = Template('UPDATE INSTALLER_PAY SET PAY = "$PAY" WHERE INSTALLER = "$INSTALLER";').substitute(
                PAY = installer_current_pay,
                INSTALLER = result[1]
            )

            cursor.execute(UpdateInstallerPayQuery)
            cursor.execute(UpdateCustomerJobIDQuery)
            cursor.execute(DeleteJobQuery)
            connection.commit()
            connection.close()

        #TODO: Deletions for all tables
        def installer_from_installers_and_keep_pay(self):
            get = INPUT()
            L_NAME, F_NAME = get.INSTALLER_AS_FOREIGN_KEY()
            deleteInstallerQuery = Template('DELETE FROM INSTALLER WHERE F_NAME = "$F_NAME" AND L_NAME = "$L_NAME";').substitute(
                F_NAME = F_NAME,
                L_NAME = L_NAME
            )
            connection.ping()
            cursor.execute(deleteInstallerQuery)
            connection.commit()
            connection.close()
        






