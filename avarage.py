print("Please enter growth all student (cm)")
students_heights=input()
list_student=students_heights.split(',')
sum=0
for element in list_student:
    sum+=int(element)
floatNumber=sum/len(list_student)
print(f"Total height {sum}")
print(f"Number of student{len(list_student)}")
print("average height "+f"%.1f" % floatNumber)