marks = []
def Uger_input():
    for i in range(5):
        marks.append(int(input()))
        
def calculate():   
    sum =0
    for i in range(len(marks)):
        sum += marks[i]        
    print("Total : ",sum)    
    print("Percentage  : ",sum/5)    
     
Uger_input()
calculate()