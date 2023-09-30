
# print("Hello world")
# def add():
#     print("Added Here ")

# # Here we are Calling a funtion 
# add()

# /////////////////////////////////////////////////////////////////


# tastCase = int(input())
# while(tastCase>0):
#     dsa = int(input())
#     toc = int(input())
#     dm = int(input())
#     dsa1 = int(input())
#     toc1 = int(input())
#     dm1 = int(input())
    
#     if(dsa+toc+dm  >  dsa1+toc1+dm1):
#         print("DRAGON")
#     elif(dsa+toc+dm  ==  dsa1+toc1+dm1):
#         if(dsa > dsa1):
#              print("DRAGON")
#         elif(dsa < dsa1):
#             print("SLOTH")
#         else:
#             if(toc > toc1):
#              print("DRAGON")
#             elif(toc < toc1):
#                 print("SLOTH")
#             else:
#                 print("TIE")
#     else:
#         print("SLOTH")
    
#     tastCase-=1
    
# /////////////////////////////////////////////


# for i in range(5):
#     for j in range(5):
#         if(j == 2):
#             print("*", sep=" ", end=" ")
#         else:     
#             print(j,sep=" ", end=" ")
#     print()
    
# ///////////////////////////////////////////////////////

# import random
# numbers= []    
# for var in range(0,11):
#     numbers.append(random.randint(1,10))
#     # print(numbers)
# for num in range(0,11):
#     for i in numbers:
#         if(i == num):
#             print(num, end=" * ")
    
            
# ///////////////////////////////////////////


# a = 10;
# while a> 0:
#     print(a)
#     a = a - 1
    
    
tuble = ("vipin" , "Ankush", "Nikhil", "Pankaj")
for iterator in tuple:
    print(iterator)