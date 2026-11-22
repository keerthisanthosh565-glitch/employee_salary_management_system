from Employee import Employee   # import the employee base class
class ContractEmployee(Employee):  # inherit from employee class
    def calculate_salary(self):    # override the salary calculation method
        total_salary = self.basic_salary+(self.basic_salary *20/100)
        print("total salary:",total_salary)
        return total_salary

    def display_detail(self):   # display details
        print("name:",self.name) # display employee detals
        print("basic salary:",self.basic_salary)
        print("work mode:",self.work_mode)
        
    
    