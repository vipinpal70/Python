# stringExample = int(input())

def minimumChange(str):
    star = 0
    hash = 0
    
    for x in str:
        if x == '*' :
            star +=1
        if x == '#' :
            hash +=1
            
    return star-hash        

ch =  minimumChange("####")    
print(ch)        
    

