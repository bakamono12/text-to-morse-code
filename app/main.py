data = morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}
ask_for_input = True
print("Type 'exit' to exit the program")
while ask_for_input:
    user_input = input("\nEnter a word or sentence to convert to morse code: ")
    if user_input == "exit":
        ask_for_input = False
    else:
        user_input = user_input.upper()
        user_input = list(user_input)
        for i in user_input:
            if i == " ":
                print(" ")
            else:
                print(data[i], end=" ")
