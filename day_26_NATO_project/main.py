student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)
# Keyword Method with iterrows()
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)


def generate_phonetic():
    user_input = input("Please, type a word: ").upper()
    try:
        nato_list = [nato_dict[word] for word in user_input]
    except KeyError as err:
        print(f"The key {err} is not alphabetic")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
