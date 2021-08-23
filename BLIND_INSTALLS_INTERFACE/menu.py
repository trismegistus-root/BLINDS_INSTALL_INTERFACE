class Menu:

    def main(self):
        option = int(input("\n[0] Customers\n[1] Jobs \n[2] Designers\n[3] Installers\n[4] Exit\n: "))
        return option
    
    def customer(self):
        option = int(input("\n[0] Add new customer\n[1] Update customer info\n[2] Search for customer\n[3] Show all customers\n[4] Main Menu\n: "))
        return option

    def jobs(self):
        option = int(input("\n[0] Update job info\n[1] Search for job\n[2] Show all jobs\n[3] Show all ready to schedule jobs\n[4] Show all jobs by installer\n[5] Mark job complete\n[6] Main Menu\n: "))
        return option
    
    def designers(self):
        option = int(input("\n[0] Add new designer\n[1] Update designer info\n[2] Search for designer\n[3] Show all designers\n[4] Main Menu\n: "))
        return option
    
    def installers(self):
        option = int(input("\n[0] Add new installer\n[1] Update installer info\n[2] Search for installer\n[3] Show all installers\n[4] Delete Installer, but track pay\n[5] Main Menu\n: "))
        return option

    class JOB_MENUS:
        def update_blind_and_box_count(self):
            option = int(input("\n[0] Update box count\n[1] Update blind count\n[2] Go Back\n: "))
            return option

    
    class TERMINATE_MENU:
        main = 4
        customer = 4
        jobs = 6
        designers = 4
        installers = 5
        update_blind_and_box_count = 2