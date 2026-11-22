
from PermanentEmployee import PermanentEmployee  #import from permanent employee class 
from ContractEmployee import ContractEmployee       # import from contract employee class
contractemoloyee=ContractEmployee("keerthi",10000,"contract") # display details of contract employee
contractemoloyee.display_detail()

contractemoloyee.calculate_salary()  # salary calculation of contract employee
 




permanentemoloyee=PermanentEmployee("keerthi",200000,"permanent")  # display details of permanent employee
permanentemoloyee.display_detail()

permanentemoloyee.calculate_salary() 

