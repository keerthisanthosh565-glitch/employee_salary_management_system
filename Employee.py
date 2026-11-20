from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_detail(self):
        pass

    
    def __init__(self,name,basic_salary,work_mode):
        self.name = name
        self.__basic_salary = basic_salary
        self.work_mode = work_mode

    @property
    def basic_salary(self):
        return self.__basic_salary

        