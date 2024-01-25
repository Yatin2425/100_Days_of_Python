import pandas as pd
#TODO 1. Create a dictionary in this format:
alphabet_list = pd.read_csv("/Users/yatintyagi/100_Days_of_Python/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dictionary  = { row.letter : row.code for (index , row ) in alphabet_list.iterrows() } 
# print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the code word: ").upper()
output_list = [dictionary[letter] for letter in word ]
print(output_list)

