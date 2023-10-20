import math
print('Hello')
print('Please Enter the width : ')
wall_width=int(input())
print('Please Enter the height : ')
wall_height=int(input())





def paintCalc(height,width):
     coverage = 5
     number_of_can = (height * width)/coverage
     print(math.ceil(number_of_can))



paintCalc(wall_height,wall_width)