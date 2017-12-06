from vehicle import *
from customer import *
from collections import defaultdict

class Employee(object):
    emp_id = 0

    def __init__(self, name):
        self.__name = name
        self.__id = self.emp_id + 1

    def __str__(self):
        return self.__name + " is of type " + self.get_title()

    def get_name(self):
        return self.__name

    def get_title(self):
        return "Subordinate"


class Manager(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def get_title(self):
        return "Manager"

    def get_sales_report(self, salesman):
        print(salesman.get_name() + "'s current cumulative sales:")
        try:
            print(sum(salesman.sales[salesman]))
        except KeyError:
            print(salesman.get_name(), "does not have any sales yet/ is not in the sales dict!")



class Salesman(Employee):
    sales = {}

    def __init__(self, name):
        Employee.__init__(self, name)

    def sale(self, vehicle, sales_price, customer):
        if customer.get_score():
            Salesman.sales.setdefault(self, []).append(sales_price)


        else:
            print("You do not have enough credit score!")


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric)  # expected output: Employee: Eric is of type Manager
print(Kyle)  # expected output: Employee: Kyle is of type Subordinate
print(Stan)  # expected output: Employee: Stan is of type Subordinate
print(Kenny)  # expected output: Employee: Kenny is of type Subordinate
print(Craig)  # expected output: Employee: Craig is of type Subordinate

## registering sales

Kenny.sale(Veh2, 6000, Heidi)
Stan.sale(Veh1, 9000, Wendy)

## printing an individual sales report:
Eric.get_sales_report(Stan)
# expected output:
# Kenny's current cumulative sales:
# 6000
