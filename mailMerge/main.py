import os

# Read the content of the starting letter
with open("mailMerge/Input/Letters/starting_letter.txt", "r") as f:
    content = f.read()

# Read the names from the file
with open("mailMerge/Input/Names/invited_names.txt", "r") as f:
    names = f.read().splitlines()
print(names)
# Specify the existing "ReadyToSend" folder
output_folder = "mailMerge/Output/ReadyToSend"

# Generate personalized letters and save them in the existing "ReadyToSend" folder
for name in names:
    personalized_content = content.replace("[name]", name)

    # Create a file for each letter with a unique name in the existing "ReadyToSend" folder
    output_file_path = os.path.join(output_folder, f"letter_for_{name}.txt")

    # Write the personalized content to the file
    with open(output_file_path, "w") as output_file:
        output_file.write(personalized_content)
