# Create a class Programmer for storing information of few programmer working at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

Sachin = Programmer("Sachin", "Skype")
Piyush = Programmer("Piyush", "Github")
Sachin.getInfo()
Piyush.getInfo()