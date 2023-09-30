# This is related to file Handing

# opening a file

# File object = open( <fileName> , <access-mode>, <buffering> )

# r   -->  ReadOnly  , default opening , no access mode
# rb   -->  ReadOnly  , binary format only ,
# r+   -->  Read and write
# rb+   -->  Read and write , binary format only
# w   -->  Write only , overwrite file
# w+   -->  Write  and Read , binay format , overwrite file
# wb   -->  Write  only , binay format , overwrite file
# wb+   -->  Write  only , binay format , overwrite file
# a   -->  append  only , pointer at the end of the previously written file ,
# ab   -->  append  only ,binary format ,  pointer at the end of the previously written file ,
# a+   -->  append and read  ,  pointer at the end of the previously written file ,
# ab+   -->  append and read , binary format ,  pointer at the end of the previously written file ,


# Example of opeing file

# fileptr = open('file.txt','w')
# if fileptr:
#     print('File opened successfully')

# fileptr.close()  # closing file


# try:
#     fileptr = open('file1.txt','w')
#     if fileptr:
#         print('File opened successfully')

# finally:
#     fileptr.close


# With statement in file Handing

# with open('file.txt','r') as fileptr:
#     content = fileptr.read()
#     print(content)

# print('File 1 opened successfully')


# writing into the file

# with open('file.txt','w') as fileptr:
#     fileptr.write('Hello World \nNow in lived in the vit bhoapl ')

# NOte :  -->  when we open file with keyword NO need to closed the file object

