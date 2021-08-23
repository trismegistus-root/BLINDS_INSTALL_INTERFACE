"""
class INPUT is a class of prompts for SQL queries that are common throughout the interface. 
TODO: Add error correcting
"""

import hashlib
import pandas as pd
from tabulate import tabulate
from alert_colors import colors

class INPUT:
    def F_NAME(self, who_called):
        string = str(input("Enter %s first name: " % who_called))
        return string
    def L_NAME(self, who_called):
        string = str(input("Enter %s last name: " % who_called))
        return string
    def ADDRESS(self, who_called):
        string = str(input("Enter %s address: " % who_called))
        return string
    def EMAIL(self, who_called):
        string = str(input("Enter %s email: " % who_called))
        return string
    def PHONE(self, who_called):
        string = str(input("Enter %s phone number: " % who_called))
        return string
    def AVAILABILITY(self):
        string = str(input("Enter window of availability: "))
        return string
    def BOXES_IN(self):
        integer = int(input("Enter number of boxes received: "))
        return integer
    def TOTAL_BOXES(self):
        integer = int(input("Enter number of boxes needed to complete job: "))
        return integer
    def BLINDS_ON_HAND(self):
        integer = int(input("Enter number of blinds received: "))
        return integer
    def BLIND_COUNT(self):
        integer = int(input("Enter number of blinds needed to complete job: "))
        return integer
    def COMPANY(self):
        string = str(input("Enter designer's company: "))
        return string
    def AREA(self):
        string = str(input("Enter designer area: "))
        return string
    def PAYS(self):
        _float = float(input("Enter how much the job pays: "))
        return _float
    def READY_TO_SCHEDULE(self, BOXES_IN, TOTAL_BOXES):
        truth = BOXES_IN == TOTAL_BOXES
        if truth:
            return 1
        else:
            return 0
    def CUSTOMER_AS_FOREIGN_KEY(self):
        who = "customer"
        f_name = self.F_NAME(who)
        l_name = self.L_NAME(who)
        return l_name,f_name
    def DESIGNER_AS_FOREIGN_KEY(self):
        who = "designer"
        f_name = self.F_NAME(who)
        l_name = self.L_NAME(who)
        return l_name, f_name
    def INSTALLER_AS_FOREIGN_KEY(self):
        who = "installer"
        f_name = self.F_NAME(who)
        l_name = self.L_NAME(who)
        return l_name, f_name
    def SCOPE(self):
        string = str(input("NOTES (Leave empty if None): "))
        if string is None:
            return "None"
        return string
    def JOB_ID(self, string):
        job_id = hashlib.sha256(string.encode())
        return str(job_id.hexdigest())
    def NEW_NUMBER(self, who_called):
        integer = int(input("How many %s do you want to add to the count: " % who_called))
        return integer
    def PANDAS_TABULATED_DATAFRAME(self, rows, column_stacks):
        df = pd.DataFrame(
            rows, columns = column_stacks
        )
        table = tabulate(df, headers = column_stacks, tablefmt = 'psql')
        return table
    def TABULATE_UNIQUE_QUERY(self, df, heads):
        table = tabulate(df, headers = heads, tablefmt = 'psql')
        return table

    class and_print:
        def COLORIZED_TABLE(self, table):
            print("\n", f"{colors.TABLE}{table}{colors.ENDC}\n")

    