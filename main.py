import pandas

PHONETIC_ALPHABET_FILE = "nato_phonetic_alphabet.csv"

phonetic_alphabet_df = pandas.read_csv(PHONETIC_ALPHABET_FILE)
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_df.iterrows()}

users_word = input("Enter a word: ")
result = [phonetic_alphabet_dict[letter] for letter in users_word.upper()]
print(result)
