class Employee:
    company = "Google"
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
    def getInfo(self):
        print(f"The employee name is {self.name}")
        print(f"The employee salary is {self.salary}")
        print(f"The employee subunit is {self.subunit}")
akash = Employee("Akash",30000,"Youtube")
akash.getInfo()