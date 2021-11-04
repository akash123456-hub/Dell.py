class Programmer:
    company = "Google"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
akash = Programmer("Akash","youtube")
vijay = Programmer("Vijay","Gpay")
akash.getInfo()
vijay.getInfo()