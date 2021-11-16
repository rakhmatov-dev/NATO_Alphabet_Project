import pandas

PHONETIC_ALPHABET_FILE = "/Volumes/Extreme SSD/Python Bootcamp/Day 26/Mac/NATO Alphabet Project/nato_phonetic_alphabet.csv"

phonetic_alphabet_df = pandas.read_csv(PHONETIC_ALPHABET_FILE)
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_df.iterrows()}


def convert_into_nato():
    users_word = input("Enter a word: ")
    try:
        result = [phonetic_alphabet_dict[letter] for letter in users_word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        convert_into_nato()
    else:
        print(result)


convert_into_nato()
