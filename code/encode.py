# list alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print block
direction = input("Please, type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your massage :\n").lower()
shift = int(input('Type the shift number: \n'))

    
# encode massage function
def encode(text,shift):
    encode_text=''
    for letter in text:
            position=alphabet.index(letter)
            new_position=position+shift
            new_letter=alphabet[new_position]
            encode_text+=new_letter
    print(encode_text)
    
    
def decode(encode_text,shift):
     decode_text=''
     for letter in encode_text:
         position=alphabet.index(letter)
         new_position=position-shift
         new_letter=alphabet[new_position]
         decode_text+=new_letter
     print(decode_text)
             
    

if direction == 'encode':
    encode(text,shift)
elif direction == 'decode':
    decode(text,shift)
else:
    print('you did not choose anything')
    
    
    
