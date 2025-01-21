#Write a Python program to create a class named Car.
# Define attributes like brand, model, and year.
# Create an object of the class and display the details of the car?
from itertools import filterfalse


# class student:
#     name = "kapil"
#
# s1 = student()
# print(s1)
# print(s1.name)

# class car:
#     Name = "BMW"
#     Model = "XM"
#     Year = "2024"
# c1 = car
# print ("Car Name is:" , c1.Name , "Car Model is:" , c1.Model , "Car Year is:" , c1.Year)

#Create a class Student with attributes name, roll_number, and marks.
#Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class Student:
#
#     def __init__(self,fullname,roll_number,marks):
#         self.name = fullname
#         self.roll_number = roll_number
#         self.marks = marks
#
#
# c1 = Student ("mukesh kumar","55",98)
# c2 = Student ("kapil kumar","55",97)
# print (c1.name,c1.roll_number,c1.marks)
# print (c2.name,c2.roll_number,c2.marks)


# Create a class Rectangle with attributes length and breadth.
# Include methods to calculate the area and perimeter of the rectangle.
# Create multiple objects and display the area and perimeter for each?

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#         pmeter = 2*(length + breadth)
#         self.pmeter = pmeter
#         area = (length*breadth)
#         self.area = area
#
# l1 = Rectangle (5,6)
# l2 = Rectangle (8,9)
# l3 = Rectangle (10,50)
#
# print("Area of rectangle-1 is :", l1.area)
# print ("Perimeter of rectangle-1 is :", l1.pmeter)
# print("Area of rectangle-2 is :", l2.area)
# print ("Perimeter of rectangle-2 is :", l2.pmeter)
# print("Area of rectangle-3 is :", l3.area)
# print ("Perimeter of rectangle-3 is :", l3.pmeter)

#Write a class Circle with an attribute radius and methods get_area() and get_circumference().
# These methods should return the area and circumference of the circle, respectively ?


# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#         area = 3.14*(radius**2)
#         self.area = area
#         cmf = 2*(3.14*radius)
#         self.cmf = cmf
#
# c1 = Circle (5)
# c2 = Circle  (4)
# print( "Area of the circle is:" , c1.area)
# print ("CMF of the circle is :",c2.cmf)

# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# class Account:
#     def __init__(self,balance,account_no):
#         self.balance=balance
#         self.account_no=account_no
#         # self.balance1=False
#         # self.debit=False
#         # self.credit=False
#
#     def Accountcheck(self):
#         self.balance1=True
#         self.debit=True
#         self.credit=True
#         print("Your account is having money")
#
# Account1=Account(2222,3444)
# print (Account1.balance , Account1.account_no)
# Account1.Accountcheck()





#     def hello(self):
#         print("Hello",self.name)
# s1 = Student("Kapil")
# s1.hello()

# 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# class Account:
#     balance = 20000
#     Account_no= 234567
#     def debit(self,d_amount):
#         self.d_amount=d_amount
#         if self.balance-d_amount>0:
#             return self.balance-d_amount
#         else:
#             return "Insufficient balance"
#     def credit(self,c_amount):
#         self.c_amount=c_amount
#         self.balance+=c_amount
#         return self.balance
# cre_amt=abs(int(input("Enter Amount to Credit:")))
# deb_amt=abs(int(input("Enter Amount to Debit:")))
# my_acc=Account()
# print("Amount after Credit:",my_acc.credit(cre_amt))
# print("Amount after Debit:",my_acc.debit(deb_amt))


# 6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count()
# to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
class Employee:
    employee_count=0
    def increment_employee_count(self):
        Employee.employee_count+=1
    def __init__(self,name,designation,joining_yr):
        self.name=name
        self.designation=designation
        self.joining_yr=joining_yr
        self.increment_employee_count()
    def show(self):
        print("Employee Name:", self.name)
        print("Employee Designation:", self.designation)
        print("Employee Joining Year:",self.joining_yr)
        print("Number of Employees:",Employee.employee_count)
e1=Employee("Shobhit","RF",2017)
e1.show()
e2=Employee("Kapil","RF",2018)
e2.show()
e3=Employee("Rahul","RF",2019)
e3.show()

