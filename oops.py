# This is oops related code 

# class

    # class ClassName:
    #statement code
    
    # example  ---->
    
        # class Person:
        #     def __init__(self, name, age):
        #         self.name = name
        #         self.age = age
        #     def display(self):
        #         print(self.name, self.age)
        # p1 = Person("John", 25)
        # p1.display()
    
# Object
    # <objectName> = <className>(argumenst)
    # example  --->
    
    # class Employee:
    #     id = 10
    #     name = 'john'
    #     def displayEmp(self):
    #         print('Id: %d\nName: %s'%(self.id, self.name))
    # emp = Employee()
    # emp.displayEmp()        
            
    
    # for delete a object use del keyword       ---> del objectName
    
    
# constructor 
    # 1. Parameterized
    # 2. Non-parameterized
    
    
    # 1. Parameterized
    
        # class Employee:
        #     def __init__(self, id, name):
        #         self.id = id
        #         self.name = name
        #     def displayEmp(self):
        #         print('Id: %d\nName: %s'%(self.id, self.name))
        # emp = Employee(10, 'john')
        # emp.displayEmp()
        
    # 2. Non-parameterized
    
        # class Employee:
        #     def __init__(self):
        #         self.id = 10
        #         self.name = 'john'
        
# Constructor Overloading is not allowed in Python

#  __dict__   ---> dictionary containing info about the class namespace
#  __doc__   ----> string which has the class documentation 
#  __name__  ----> used to access the class name
#  __module__  ---> access the module 
# __bases__   ---> contains a tuple including all base classes

        
# Inheritance 
    # class derive-class (<base-class1>,<base-class2, ...>)
    # <class-suite>
    
    # Single , Multiple , multiLevel , hierarchical , hybrid
    
    
    # example  --->
    
        # class Employee:
        #     def __init__(self, id, name):
        #         self.id = id
        #         self.name = name
        #     def displayEmp(self):
        #         print('Id: %d\nName: %s'%(self.id, self.name))
        # emp = Employee(10, 'john')
        # emp.displayEmp()
        
        
        # class Manager(Employee):
        #     def __init__(self, id, name, salary):
        #         Employee.__init__(self, id, name)
        #         self.salary = salary
        #     def displaySalary(self):
        


# Method overloading Example

    # class Animal:
    #     def __init__(self):
    #         def speak(self):
    #             print('Animal speak')
    
    # class Dog(Animal):
    #     def  speak(self):
    #         print('Barking')
            
    # d = Dog()
    # d.speak()
    
    
 # we can also perform data hiding by adding the double underscore (___) as a prefix to the attribute which is to be hidden. After this, the attribute will not be visible outside of the class through the object.
 
        # class Employee:  
        #     __count = 0;  
        #     def __init__(self):  
        #         Employee.__count = Employee.__count+1  
        #     def display(self):  
        #         print("The number of employees",Employee.__count)  
        # emp = Employee()  
        # emp2 = Employee()  
        # try:  
        #     print(emp.__count)  
        # finally:  
        #     emp.display()  
                                        
            
    
    
# class student:
    
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def display(self):
#         print(self.name, self.rollno, self.marks)
            

# s1 = student("Vipin",10064,82.2)            
# s2 = student("Ak",10161,78.2)
# s1.display()            
# s2.display()
# print(s1.__doc__)            
# print(s1.__dict__)     
# print(s1.__module__)       




class Polygon:
    __width = None
    __height = None

    def set_values(self, width, height):
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2

rect = Rectangle()
tri = Triangle()
rect.set_values(50, 40)
tri.set_values(50, 40)
print(rect.area())
print(tri.area())





