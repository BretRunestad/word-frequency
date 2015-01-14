with open("newsample.txt") as file:
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
cleanlist = cleanstring.split()

#print(cleanstring)
#print(cleanlist)

def word_count(a_list):
    a_dict = {}
    for item in a_list:
        if item in a_dict:
            a_dict[item]+= 1
        else:
            a_dict[item] = 1
    return a_dict

book_dict = word_count(cleanlist)

#print(book_dict)

def top_20(a_dict):
    """a function that takes a dictionary with words for keys and the number of times those words appear
    in the text as values.  This function returns a list of dictionaries of the 20 most-used words"""
    sorted_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[1:21]

winners = top_20(book_dict)

#print(winners)

print("{}  {}".format((winners[0])[0], (winners[0])[1]))
