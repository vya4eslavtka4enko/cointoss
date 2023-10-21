print('hello')
print("Enter the number what you chedk ")
number = int(input())

def checkFunc(number):
    is_Prime = True
    for i in range(2,number):
        if number % i == 0:
            is_Prime=False
    if is_Prime:
        print('This is Prime Number')
    else:
        print('This is not Prime Number')
    print(is_Prime)
checkFunc(number)