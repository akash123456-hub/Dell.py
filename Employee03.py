class Employee:
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
    def getInfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print(f"Good Morning Sir!")
    @staticmethod
    def time():
        print(f"The time is 9 AM in the morning")
akash = Employee("Akash",30000,"Youtube")
akash.getInfo()
akash.greet()
akash.time()