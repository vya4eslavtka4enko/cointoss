import random
words_list=['babon','enot','reber','efoure']
computer_choose = random.randint(0,len(words_list)-1)
# function printBlank
def printBlank():
    print('[',end="")
    for n in range(len(words_list[computer_choose])):
        print(' - ',end="")
    print(']')
# --------------------
print("guess the letter ")
user_letter = input()
# print(user_letter)

def seeking_letter(word,element):
    for position in range():
      

# print(words_list[computer_choose])
# printBlank()
seeking_letter(words_list[computer_choose],user_letter)
