import pandas

data = pandas.read_csv("projects/nato-alphabet/alphabet.csv")

# TODO 1. Create a dictionary in this format:
dictionary = {row.letter:row.code for (_, row) in data.iterrows()}
print(dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

phonetic_code = [dictionary[letter] for letter in word]

print(phonetic_code)
