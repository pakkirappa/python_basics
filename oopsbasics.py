# OOPS  
# 1. Class
# 2. Object
# 3. Inheritance
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction

# Class
# class Person:  
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# class  Person:
#     def __init__(self, name,age):
#         self.name=name
#         self.age=age
    
class Computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram= ram
    def config(self):
        print("COnfig is "+ self.ram , self.cpu)
        
com1= Computer("15 GB", "1 TB")
# com2= Computer()
com1.config()
print(id(com1))  # it will store in heap memory
# print(com1)



