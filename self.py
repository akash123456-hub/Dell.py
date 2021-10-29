class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
akash = Employee()
akash.salary = 30000
akash.getSalary()