# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# #data = pandas.read_csv("nato_phonetic_alphabet.csv.csv")
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#    # print(row.student)
#    # print(row.score)
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")


dict_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
# print(dict_alphabet)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dict_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()