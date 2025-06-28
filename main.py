with open("./Input/Letters/starting_letter.txt") as file:
    letter_data = file.read()

with open("./Input/Names/invited_names.txt") as file:
    for name in file:
        custom_letter = letter_data.replace("[name]", name.strip())
        letter = f"./Output/ReadyToSend/{name.strip()}'s letter.txt"
        with open(letter, mode="w") as output_file:
            output_file.write(custom_letter)