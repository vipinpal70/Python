# import os

# a = int(input())   # Taking User Input 1
# b = int(input())   # Taking User Input 2
# def swapWithvar(a,b):  # defing function
#     temp = a  # assigning value to temp var
#     a = b      # assigning value b  to a 
#     b = temp    # assigning value temp  to b
#     print("with Temp variable a = " ,a)  # printing values
#     print( "b = ",b)
 
 
    
# def swapWithoutVar(a,b):  # defing function
#     a, b = b, a    # assigning value b  to a  and assigning value b  to a 
#     print("without Temp variable a = " ,a)   # printing values
#     print( "b = ",b)
       
# swapWithvar(a,b)  # calling Function Herer
# swapWithoutVar(a,b)   # calling Function Herer
 
 
 
 
# define the range of numbers
# start = 0
# stop = 10
# step = 1

# create a list of numbers using range and for loop
# numbers = [i for i in range(start, stop, step)]

# print the list of numbers
# print(numbers)

# NUM = 13 

# def CHE():
#     global NUM  
#     # NUM = 1
#     print(NUM)
    
# CHE()
# print(NUM)    




# def separate_elements(input_list):  # We are defining function here
#     odd_list = []               # This old List
#     even_list = []              # This is even List
    
#     for index, element in enumerate(input_list):        # loop for accessing lists elements
#         if index % 2 == 0:                              # condition for even number
#             even_list.append(element)                   # adding number to even list
#         else:
#             odd_list.append(element)                    # adding number to odd list
    
#     return even_list, odd_list                          # returning both list here

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]               # This is list to check
# even, odd = separate_elements(my_list)                  # Passing my_list to the function and function return 2 lists

# print("Elements at even index positions:", even)        # Printing Even list here
# print("Elements at odd index positions:", odd)          # Printing Odd list Here







# Create a new Python file in the same directory as my_module.py.
# Import the my_module module using the import statement.







# import my_module   # import my module here 

# # Perform arithmetic operations
# result_add = my_module.add(5, 3)                # Addition Here
# result_subtract = my_module.subtract(10, 4)     # Subtraction Here
# result_multiply = my_module.multiply(6, 7)      # Multiplication Here
# result_divide = my_module.divide(20, 5)         # Division  Here


# # Printing the Values here 
# print("Addition:", result_add)
# print("Subtraction:", result_subtract)
# print("Multiplication:", result_multiply)
# print("Division:", result_divide)

# # Generate a random number
# random_number = my_module.generate_random_number()
# print("Random Number:", random_number)



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
    
    
    
# def is_prime(num):  # Function Define Here
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_prime_numbers(n):  # Functoin for Printing Prime Values
#     count = 0
#     num = 2
#     while count < n:         # Loop for accees all elements 
#         if is_prime(num):
#             print(num, end=" ")
#             count += 1
#         num += 1

# n = int(input("Enter the value of n: "))   # taking input from the User
# print("First", n, "prime numbers are:")    # printing values here
# print_prime_numbers(n)
    
  
    
    
# def multiply_matrices(matrix1, matrix2):
#     rows1 = len(matrix1)
#     cols1 = len(matrix1[0])
#     rows2 = len(matrix2)
#     cols2 = len(matrix2[0])

#     if cols1 != rows2:
#         print("Cannot multiply the matrices. Invalid dimensions.")
#         return None

#     result = [[0 for _ in range(cols2)] for _ in range(rows1)]

#     for i in range(rows1):
#         for j in range(cols2):
#             for k in range(cols1):
#                 result[i][j] += matrix1[i][k] * matrix2[k][j]

#     return result

# # Example matrices
# matrix1 = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

# matrix2 = [[10, 11],
#            [12, 13],
#            [14, 15]]

# result = multiply_matrices(matrix1, matrix2)

# if result is not None:
#     print("Result of matrix multiplication:")
#     for row in result:
#         print(row)


   
    #  Big Data Assignment   -------> 
     
# class productInfo:
#     def __init__(self ,Product_Id , Product_Name , Price ):
#         self.Product_Id = Product_Id
#         self.Product_Name = Product_Name
#         self.Price = Price
#     def display(self):
#         print(self.Product_Id , self.Product_Name , self.Price)    
        
# obj1 = productInfo(10025,'       Laptop       ' , 40000)           
# obj2 = productInfo(20036,'       LED TV       ' , 30000)           
# obj3 = productInfo(15872,'   Air Conditioner  ',  35000)
# print('\n Id           Name         Price')
# obj1.display()           
# obj2.display()           
# obj3.display()  
# print('\n')         ------> End



# function to count the word which is this 
# to count how many Uppercase characters
# 


