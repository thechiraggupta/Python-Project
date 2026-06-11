logo = '''        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           

              '''

print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter not in alphabets:
            cipher_text += letter
        else:
            position = alphabets.index(letter) + shift_amount
            position %= len(alphabets)
            cipher_text += alphabets[position]

    print(f"Here is the encoded result: {cipher_text}")


def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            position = alphabets.index(letter) - shift_amount
            position %= len(alphabets)
            output_text += alphabets[position]

    print(f"Here is the decoded result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    if direction == "encode":
        encrypt(text, shift)

    elif direction == "decode":
        decrypt(text, shift)

    else:
        print("INVALID INPUT")

    restart = input(
        "\nType 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")