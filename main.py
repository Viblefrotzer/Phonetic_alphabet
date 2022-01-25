# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# main cycle
in_progress = True
while in_progress:
    # input your word
    word = input("Enter a word: ").upper()
    # trying to divide it into letters using phonetic dictionary
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    # catching errors
    except KeyError:
        print("No digit allowed")
    else:
        print(output_list)
        in_progress = False
# print(output_list)
