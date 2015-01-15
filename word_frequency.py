with open("sample.txt") as file:
    all_lines = file.readlines()

#print(all_lines)

rawstring = ' '.join(all_lines)

#print(rawstring)

def clean(text):
    """A function to clean text of various punctuations, and to replace hyphens with spaces"""
    for char in """.$#,:"'?!)(""":
        text = text.replace(char, "")
    for char in """-""":
        text = text.replace(char, " ")
    return text

cleanstring = clean(rawstring).lower()

#print(cleanstring)


def word_frequency(a_string):
    """a function that takes a string and creates a dictionary
    where the keys are the independent words in the string and
    their values are the number of times that word appears in
    the string"""
    a_list = a_string.split()
    a_dict = {}
    for item in a_list:
        if item in a_dict:
            a_dict[item]+= 1
        else:
            a_dict[item] = 1
    return a_dict

book_dict = word_frequency(cleanstring)

#print(book_dict)

def top_20(a_dict):
    """a function that takes a dictionary with words for keys and the number of times those words appear
    in the text as values.  This function returns a list of dictionaries of the 20 most-used words"""
    sorted_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[1:21]

winners = top_20(book_dict)

#print(winners)

def basic_print(lista):
    """a function that prints the first two values of a list of tuples
    with each tuple on its own line, and the two values separated by
    two spaces"""
    for item in lista:
        print("{}  {}".format(item[0], item[1]))

basic_print(winners)
