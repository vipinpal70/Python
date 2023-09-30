# This is lambda relatead codes

# lambda arguments : expression

add = lambda num : num +10
print(add(10))


list_ = [34,12,64,55,75,13,63]
oddList = list(filter(lambda num : (num % 2 != 0),list_ ))
print(oddList)


number_list = [2,4,5,1,3,7,8,9,10]
squareList = list(map(lambda num : num**2,number_list))
print(squareList)


square_List = [lambda num : num**2 for num in range(0,11)]
for square in square_List:
    print(square(2),end="  ")
    
    
print(sep="\n",)    
minimum = lambda x,y: x  if(x<y) else y 
print(minimum(35,74))   


