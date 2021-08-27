from cursor import cursor, connection
from inputs import INPUT
from string import Template
import pandas as pd
from menu import Menu
from data_columns import COLUMN
from alert_colors import colors
from queries import QUERY
from forms import FORM


QUERY = QUERY()
columns = COLUMN()
get = INPUT()

class SQL_INTERFACE:
    class show_all:
        def customers(self):
            connection.ping()
            sql = QUERY.CUSTOMER().SELECT().WHOLE_TABLE().WITHOUT_JOBID()
            cursor.execute(sql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, columns._customer_without_jobID)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()

        def jobs(self):
            connection.ping()
            sql = QUERY.JOB().SELECT().WHOLE_TABLE().WITHOUT_JOBID()
            cursor.execute(sql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, columns._job_without_jobID)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()
        
        def designers(self):
            connection.ping()
            sql = QUERY.DESIGNER().SELECT().WHOLE_TABLE().ALL_COLUMNS()
            cursor.execute(sql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, columns._designers)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()
        
        def installers(self):
            connection.ping()
            sql = QUERY.INSTALLER().SELECT().WHOLE_TABLE().ALL_COLUMNS()
            cursor.execute(sql)
            rows = cursor.fetchall()
            table = get.PANDAS_TABULATED_DATAFRAME(rows, columns._installers)
            get.and_print().COLORIZED_TABLE(table)
            connection.commit()
            connection.close()

    class add_new:
        def job(self):
            L_NAME, F_NAME, CUSTOMER, DESIGNER, INSTALLER, PAYS, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE, JOB_ID = FORM.JOB().NEW_JOB()
            sql = QUERY.JOB().INSERT().NEW_JOB(JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE)
            connection.ping()
            cursor.execute(sql)
            connection.commit()
            connection.close()
            return L_NAME, F_NAME, DESIGNER, JOB_ID

        def customer(self):
            L_NAME, F_NAME, DESIGNER, JOB_ID = self.job()
            ADDRESS, EMAIL, PHONE, AVAILABILITY = FORM.CUSTOMER().NEW_CUSTOMER_AFTER_NEW_JOB()
            sql = QUERY.CUSTOMER().INSERT().NEW_CUSTOMER(F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER, JOB_ID)
            connection.ping()
            cursor.execute(sql)
            connection.commit()
            connection.close()
        
        def designer(self):
            L_NAME, F_NAME, EMAIL, PHONE, COMPANY, AREA = FORM.DESIGNER().NEW_DESIGNER()
            sql = QUERY.DESIGNER().INSERT().NEW_DESIGNER(F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA)
            connection.ping()
            cursor.execute(sql)
            connection.commit()
            connection.close()

        def installer(self):
            L_NAME, F_NAME, PHONE, EMAIL = FORM.INSTALLER().NEW_INSTALLER()
            sql = QUERY.INSTALLER().INSERT().NEW_INSTALLER(F_NAME, L_NAME, PHONE, EMAIL)
            initialize_installer_pay = QUERY.INSTALLER_PAY().INSERT().NEW_INSTALLER(L_NAME, F_NAME)
            connection.ping()
            cursor.execute(sql)
            cursor.execute(initialize_installer_pay)
            connection.commit()
            connection.close()
    
    class search_for:
        class customer:
            def by_name(self):
                L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
                CustomerSearchQuery = QUERY.CUSTOMER().SELECT().BY_NAME(F_NAME, L_NAME)
                connection.ping()
                cursor.execute(CustomerSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, columns._customers)
                get.and_print().COLORIZED_TABLE(table)
                return result

        class job:
            def by_customer_name(self):
                CUSTOMER = get.CUSTOMER_AS_FOREIGN_KEY()
                JobSearchQuery = QUERY.JOB().SELECT().BY_CUSTOMER_NAME(CUSTOMER)
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
                return result
            
            def by_ready_to_schedule(self):
                JobSearchQuery = QUERY.JOB().SELECT().BY_READY_TO_SCHEDULE()
                connection.ping()
                cursor.execute(JobSearchQuery)
                result = cursor.fetchall()
                table = get.PANDAS_TABULATED_DATAFRAME(result, columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
            
            def by_installer(self):
                connection.ping()
                INSTALLER = get.INSTALLER_AS_FOREIGN_KEY()
                JobTableSql = QUERY.JOB().SELECT().BY_INSTALLER(INSTALLER)
                cursor.execute(JobTableSql)
                rows = cursor.fetchall()
                table = get.PANDAS_TABULATED_DATAFRAME(rows, columns._job_without_jobID)
                get.and_print().COLORIZED_TABLE(table)
                connection.commit()
                connection.close()

        class designer:
            def by_name(self):
                L_NAME, F_NAME = get.DESIGNER_AS_FOREIGN_KEY()
                DesignerSearchQuery = QUERY.DESIGNER().SELECT().BY_NAME(F_NAME, L_NAME)
                connection.ping()
                cursor.execute(DesignerSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, columns._designers)
                get.and_print().COLORIZED_TABLE(table)
                return result
        
        class installer:
            def by_name(self):
                L_NAME, F_NAME = get.INSTALLER_AS_FOREIGN_KEY()
                InstallerSearchQuery = QUERY.INSTALLER().SELECT().BY_NAME(F_NAME, L_NAME)
                connection.ping()
                cursor.execute(InstallerSearchQuery)
                result = cursor.fetchone()
                table = get.PANDAS_TABULATED_DATAFRAME(result, columns._installers)
                get.and_print().COLORIZED_TABLE(table)
                return result

    class update:
        class job:
            def blind_and_box_count(self):
                """ PATTERN: Grab BOX_COUNT, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT
                             Display all gathered columns
                             Update count with INPUT() logic
                             Determine if Ready to schedule
                    UNIQUE: Queries are too unique to separate logic for future use
                """
                L_NAME, F_NAME = get.CUSTOMER_AS_FOREIGN_KEY()
                _hash = get.JOB_ID(L_NAME + F_NAME)
                query = QUERY.JOB().SELECT().BY_JOB_ID(_hash)
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
                query = QUERY.JOB().UPDATE().BOX_AND_BLIND_COUNT_MANUALLY(BOXES_IN, BLINDS_ON_HAND, READY_TO_SCHEDULE, _hash)
                connection.ping()
                cursor.execute(query)
                connection.commit()
                connection.close()
                query = QUERY.JOB().SELECT().BY_JOB_ID(_hash)
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
            
            def blind_and_box_count_by_barcode(self):
                CUSTOMER, DESIGNER, JOB_ID = FORM().CUSTOMER().ADD_BOX_UNDER_CUSTOMER_NAME()
                option = -1
                while option != Menu().TERMINATE_MENU().update_blind_and_box_count_by_barcode:
                    BARCODE = str(input("Scan barcode: "))
                    sql = QUERY.BOX().INSERT().NEW_BOX(JOB_ID, CUSTOMER, DESIGNER, BARCODE)
                    connection.ping()
                    cursor.execute(sql)
                    connection.commit()
                    connection.close()
                    option = Menu().JOB_MENUS().update_blind_and_box_count_by_barcode()
                
                

        class installer_pay:
            def and_set_to_zero(self):
                INSTALLER = get.INSTALLER_AS_FOREIGN_KEY()
                connection.ping()
                setPayToZero = QUERY.INSTALLER_PAY().UPDATE().PAY_SET_TO_ZERO(INSTALLER)
                cursor.execute(setPayToZero)
                connection.commit()
                connection.close()        

    class delete:
        class job:
            def and_update_installer_pay(self):
                """ @ PARAM: NONE
                    @ PURPOSE: Mark a job as complete by completely removing it.  
                    @ NOTES: TODO: This is a quick method for testing interface patterns.
                                   Ultimately, we will want to have a way to track past jobs, weekly pay, and "pay stubs", (pay stubs may end up being a separate .csv file)
                                   This will require a method for updating appropriate customer if they are of repeat business. 
                                   _hash is a SHA256 encryption of the concatenation of L_NAME + F_NAME of associated customer:
                                        (This means one customer cannot have two open jobs at once)
                                        (Some error checking for a multi-job customer may be necessary)
                                        (Error checking may be required for jobs that are partial-installs of parent job)
                    @ RETURNS: Job deleted from JOB table. 
                               CUSTOMER JOB_ID updated to "Complete"
                               INSTALLER_PAY updated by PAYS

                """
                _hash, L_NAME, F_NAME = FORM.JOB().ID_AND_NAMES()
                JobPayQuery = QUERY.JOB().SELECT().UNIQUE_COLUMNS().PAY_AND_INSTALLER().BY_JOB_ID(_hash)
                # Treble damages - 
                UpdateCustomerJobIDQuery = QUERY.CUSTOMER().UPDATE().JOB_ID_TO_COMPLETE(F_NAME, L_NAME)
                DeleteJobQuery = QUERY.JOB().DELETE().BY_JOB_ID(_hash)
                connection.ping()
                cursor.execute(JobPayQuery)
                result = cursor.fetchone() # result[0] = pay, result[1] = installer
                INSTALLER = result[1]
                PAY = result[0]
                connection.commit()
                getInstallerCurrentPay = QUERY.INSTALLER_PAY().SELECT().PAY(INSTALLER)
                cursor.execute(getInstallerCurrentPay)
                installer_current_pay = cursor.fetchone()
                connection.commit()
                installer_current_pay = installer_current_pay[0] + float(PAY)
                UpdateInstallerPayQuery = QUERY.INSTALLER_PAY().UPDATE().PAY(installer_current_pay, INSTALLER)
                cursor.execute(UpdateInstallerPayQuery)
                cursor.execute(UpdateCustomerJobIDQuery)
                cursor.execute(DeleteJobQuery)
                connection.commit()
                connection.close()

        #TODO: Deletions for all tables
        class installer:
            def and_keep_pay(self):
                """ As the name suggests, this function safe deletes an installer from the INSTALLER table but NOT from INSTALLER_PAY table
                """
                L_NAME, F_NAME = get.INSTALLER_AS_FOREIGN_KEY()
                deleteInstallerQuery = QUERY.INSTALLER().DELETE().BY_NAME(F_NAME, L_NAME)
                connection.ping()
                cursor.execute(deleteInstallerQuery)
                connection.commit()
                connection.close()






