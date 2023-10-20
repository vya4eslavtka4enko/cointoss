print("Please enter the number ")
number=int(input())
max_sum=0
for element in range(number+1):
    if element%2==0:
        max_sum+=element
    else:
        continue
print(max_sum)