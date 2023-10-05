"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hours = 0, hourly = 0, salary = 0, commNum = 0, commCon = 0,commBon = 0):
        self.name = name
        self.hours = hours
        self.hourly = hourly
        self.salary = salary
        self.commNum = commNum
        self.commCon = commCon
        self.commBon = commBon

    def get_pay(self):
        total_pay = self.hourly * self.hours + self.salary + self.commCon*self.commNum+self.commBon
        return total_pay

    def __str__(self):
        contract_about = ""
        commission_about = ""
        
        if self.commCon:
            commission_about += f" and receives a commission for {self.commNum} contract(s) at {self.commCon}/contract"
        elif self.commBon:
            commission_about += f" and receives a bonus commission of {self.commBon}"
        
        if self.hourly:
            contract_about = "contract"
            sentence = f"{self.name} works on a {contract_about} of {self.hours} hours at {self.hourly}/hour{commission_about}. Their total pay is {self.get_pay()}."
        elif self.salary:
            contract_about = "monthly salary"
            sentence = f"{self.name} works on a {contract_about} of {self.salary}{commission_about}. Their total pay is {self.get_pay()}."
    
        return sentence
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',hours = 100,hourly = 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',salary = 3000,commNum = 4,commCon = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',hours = 150,hourly = 25, commNum = 3,commCon = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',salary = 2000, commBon = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',hours = 120, hourly = 30, commBon = 600)