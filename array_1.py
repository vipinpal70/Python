# # this is related to array 

# import array as arr

# numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  


import  threading

def print_hello(n):
    print( "Hello ,how  old  are  you?  ", n)
    
    
T1 = threading.Thread (target = print_hello,  args = (20 ,  ) )
T1 .start()
T1.join()
print("Thank you ")