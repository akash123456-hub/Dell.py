class Employee:
    company = "Google"
    salary = 30000
akash = Employee()
sanjay = Employee()
akash.company = "Microsoft"
print(akash.company)
print(sanjay.company)