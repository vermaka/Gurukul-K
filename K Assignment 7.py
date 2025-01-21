# Assignment 1: Static Methods
# Create a class MathOperations that contains:
# A static method add_numbers that takes two arguments and returns their sum.
# class MathOperations:
#     @staticmethod
#     def add_numbers(a, b):
#         return a + b
#     @staticmethod
#     def multiply_numbers(a, b):
#         return a * b
#
# a = float(input("1st Number:"))
# b = float(input("2nd Number:"))
# result_sum = MathOperations.add_numbers(a,b)
#
# result_multiply = MathOperations.multiply_numbers(a,b)
# print(result_sum)
# print(result_multiply)




# Assignment 2: Class Methods
# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.

# class Person:
#     count = 0
#     def __init__(self):
#         Person.count = Person.count + 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def display_info(self, name, roll_number, percentage):
#         self.name=name
#         self.roll_number=roll_number
#         self.percentage=percentage
#         print("Name of Student:", self.name)
#         print("Roll number:", self.roll_number)
#         print("Marks of Student:", self.percentage)
#
# s1 = Person()
# s1.display_info("John",36,90)
# s2 = Person()
# s2.display_info("Peter",37,92)
# print("Number of Students registered till now:",Person.get_count())

# Assignment 3: Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.
#
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 8/5) + 32
#
#     @classmethod
#     def info(cls):
#         return "Temperature converted from Celsius and Fahrenheit."
#
# print("Temperature from Celsius to Fahrenheit:",TemperatureConverter.celsius_to_fahrenheit(36))
# print(TemperatureConverter.info())

# Assignment 4: Single Inheritance
# Create two classes:
# Animal with a method sound that prints "Animal sound".
# Dog that inherits from Animal and overrides the sound method to print "Bark".
#
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound1(self):
#         print("Bark")
#
# animal = Animal()
# animal.sound()
# Dog = Dog()
# Dog.sound1()

# Assignment 5: Multiple Inheritance
# Create two classes:
# Bird with a method fly that prints "Flying".
# Fish with a method swim that prints "Swimming".
# A class Duck that inherits from both Bird and Fish.

# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     def __init__(self):
#         print("Inheriting 2 classes")
#
# duck = Duck()
# duck.fly()
# duck.swim()





