from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
answer = ''

def caesar(enter_text,shift_amount,direction):
    end_text = ''
    if direction == 'decode':
        shift_amount*=-1
    for letter in enter_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        end_text+=alphabet[new_position]
    print(end_text)

while answer!='n':
    shift=int(input("Type the shift number "))
    text=input('Type you massage  ')
    direction=input("Type 'decode' or 'encode'   ")
    caesar(text,shift,direction)
    answer=input('Do you want repeat yes or no y/n ')