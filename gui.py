import os
os.system('cls')
        # !/usr/bin/python3  

        # from tkinter import * 
# import tkinter
 
#         #creating the application main window.   
# top = tkinter.Tk()  

#         #Entering the event main loop  
# top.mainloop() 


# from tkinter import *  
# parent = Tk()
# parent.geometry("300x300")
  
# name = Label(parent,text = "Name").grid(row = 0, column = 0).place(x = 50 , y = 50)  

# e1 = Entry(parent).grid(row = 0, column = 1)  

# password = Label(parent,text = "Password").grid(row = 1, column = 0)  

# e2 = Entry(parent).grid(row = 1, column = 1)  

# submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  

# parent.mainloop()  


'''
geometry methods.

The pack() method
The grid() method
The place() method




 pack() is given below.

    expand: If the expand is set to true, the widget expands to fill any space.
    Fill: By default, the fill is set to NONE. However, we can set it to X or Y to determine whether the widget contains any extra space.
    size: it represents the side of the parent to which the widget is to be placed on the window.
 

'''



from tkinter import *  
top = Tk()  
top.geometry("400x250")  
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)  
top.mainloop()   


