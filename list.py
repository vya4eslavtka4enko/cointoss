import random

print("Hello")
string_name=input("Please enter all names :  ")
list_name=string_name.split(',')
print(f'{list_name}')
random_guy=random.randint(0,len(list_name)-1)

# print(list_name.index(random_guy))
print(f'{list_name[random_guy]} is going buy meal today')
# for i in list_name:
#     print (list_name[random_guy])