PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter = letter_file.read()
    letter_contents = letter.replace("Zaki442", "Zakaria")

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as complete_letter:
            complete_letter.write(new_letter)
