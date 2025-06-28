#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as file:
    letter_data = file.read()

with open("./Input/Names/invited_names.txt") as file:
    for name in file:
        custom_letter = letter_data.replace("[name]", file.readline())
        letter = f"./Output/ReadyToSend/{name}'s letter.txt"
        with open(letter, mode="w") as output_file:
            output_file.write(custom_letter)