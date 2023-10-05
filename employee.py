"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hours, hourly, salary, commNum, commCon,commBon):
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
        if self.hourly:
            if self.commBon:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour and receives a bonus commission of {self.commBon}. Their total pay is {self.get_pay()}."
            elif self.commCon:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour and receives a commission for {self.commNum} contract(s) at {self.commCon}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour. Their total pay is {self.get_pay()}."
        elif self.salary:
            if self.commBon:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commBon}. Their total pay is {self.get_pay()}."
            elif self.commCon:
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.commNum} contract(s) at {self.commCon}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',0,0,4000,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',100,25,0,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',0,0,3000,4,200,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',150,25,0,3,220,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',0,0,2000,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',120,30,0,0,0,600)
