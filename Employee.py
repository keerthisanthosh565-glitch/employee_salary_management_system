from abc import ABC,abstractmethod
class Employee(ABC):   # import into abstract metod
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_detail(self):  # display employee details
        pass

    
    def __init__(self,name,basic_salary,work_mode):  # initalizes employee detaails
        self.name = name
        self.__basic_salary = basic_salary
        self.work_mode = work_mode

    @property
    def basic_salary(self):   # provides access to private basic salary
        return self.__basic_salary

        