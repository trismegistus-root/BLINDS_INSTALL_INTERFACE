class Menu:
    def main(self):
        option = int(input("\n[0] Customers\n[1] Jobs \n[2] Designers\n[3] Installers\n[4] Exit\n"))
        return option
    
    def customer(self):
        option = int(input("\n[0] Add new customer\n[1] Update customer info\n[2] Search for customer\n[3] Show all customers\n[4] Exit\n"))
        return option

    def jobs(self):
        option = int(input("\n[0] Add new job\n[1] Update job info\n[2] Search for job\n[3] Show all jobs\n[4] Exit\n"))
        return option
    
    def designers(self):
        option = int(input("\n[0] Add new designer\n[1] Update designer info\n[2] Search for designer\n[3] Show all designers\n[4] Exit\n"))
        return option
    
    def installers(self):
        option = int(input("\n[0] Add new installer\n[1] Update installer info\n[2] Search for installer\n[3] Show all installers\n[4] Exit\n"))
        return option
    
    def update_blind_and_box_count(self):
        option = int(input("\n[0] Update box count\n[1] Update blind count\n[2] Exit\n"))
        return option