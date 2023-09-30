# This is function related codes

def func1():  #define function here
    print("Hello World")
    
func1()    # calling function here


# perameterise function

def func2(a,b):
    print(a+b)
    
func2(10,20)


# biult-in functions


print(len("Hello World"))   # len()  method 
print(abs(-40.2))  # abs()  return positive value of a negative integer
print(abs(-30))


a = -20.83
aa = [1,3,4,6]
print(all(aa))     #all()   accepts an iterator objects like dictionary , List , 


x = 10
print(bin(x))    # bin()   return binay form of a number


bool(10)        # convert a value into boolean ( True or False)
arr = bytes("vipin",'utf-8')  #  return bytes objects
print(arr)

cl = 15
callable(cl)    # return True if the object passsed appears to be callable 

code = compile('x=5\ny=10\nprint("sum = :",x+y)','sum.py','exec')       # it takes source code as input and return a code object 
                                                                 # which can later be executed by exec() function.
                                                                 
exec(code)    #    dynamic function unlike eval() function 


print( sum([1,2,3,4,5]) )  #  get the sum of numbers 


array = [4,3,2,1]
print(any(array))   #  return true if any item in an iterable is true Otherwise , it return false


# print(ascii())   #                                     

#  bytearray()    --->  

print(eval('8+1+4/2'))  # expression code to solve 

# map()  --> 

# memoryview
# object()
# open()

# chr() 



###########################################################



# Your Unique License game key: Z5LUV-GVFB-GH4R-M89K-3RSE



###########################################################                                                            