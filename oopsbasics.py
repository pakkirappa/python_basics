# OOPS  
# 1. Class : Blueprint of the object  (Real world entity) 
# 2. Object : Instance of the class  (Real world entity)    
# 3. Inheritance    :  (Single, Multiple, Multilevel, Hierarchical, Hybrid)
# 4. Polymorphism : Many forms  (Method Overloading, Method Overriding ) 
# 5. Encapsulation : Binding the data with the code  (Data hiding) 
# 6. Abstraction : Hiding the complexity and showing the simplicity 

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



