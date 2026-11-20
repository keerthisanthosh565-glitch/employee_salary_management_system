from Employee import Employee
class PermanentEmployee(Employee):
    def calculate_salary(self):
        total_salary = self.basic_salary+(self.basic_salary *20)/100
        print("total salary:",total_salary)
        return total_salary
    def display_detail(self):
        print("name:",self.name)
        print("basic salary:",self.basic_salary)
        print("work mode:",self.work_mode)  
    
        
    