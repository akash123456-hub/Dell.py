class Employee:
    company = "Google"
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning, Sir!")
    @staticmethod
    def time():
        print("The time is 9 AM in the morning")
akash = Employee()
akash.salary = 30000
akash.getSalary("Thanks")
akash.greet()
akash.time()
