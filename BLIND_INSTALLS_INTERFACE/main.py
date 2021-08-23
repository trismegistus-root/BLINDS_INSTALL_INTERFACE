from menu import Menu
from sql_interface import SQL_INTERFACE


if __name__ == "__main__":
    please = SQL_INTERFACE()
    menu = Menu()

    option = -1
    while option != 4:

        option = menu.main() # Driver Main Variable

        if option == 0: # CUSTOMER MENUS AND FUNCTIONS
            cust_option = -1
            while cust_option != 4:
                cust_option = menu.customer()
                if cust_option == 0:
                    please.add_new().customer()
                # TODO: cust_option 1
                elif cust_option == 2:
                    please.search_for().customer().by_name() # TODO: Add other search options
                elif cust_option == 3:
                    please.show_all().customers()
                else:
                    continue

        elif option == 1: # JOB MENUS AND FUNCTIONS
            job_option = -1
            while job_option != 4:
                job_option = menu.jobs()
                if job_option == 0:
                    please.update().job().blind_and_box_count()
                elif job_option == 1:
                    please.search_for().job().by_customer_name() #search by pass the hash
                elif job_option == 2:
                    please.show_all().jobs()
                elif job_option == 3:
                    please.search_for().job().by_ready_to_schedule()
                else:
                    continue




        elif option == 2:
            designer_option = menu.designers()
        elif option == 3:
            installer_option = menu.installers()
        else:
            continue
