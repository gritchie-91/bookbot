
#takes in a file and returns text as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

#takes a string of text and returns a number of words in string
def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

#takes a string of text and returns the number of each character that appears
def char_count(text):
    chars = {}
    for char in text:
        c = char.lower()
        if(c in chars):
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    for c in dict:
        new_dict = {}
        new_dict["char"] = c
        new_dict["num"] = dict[c]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list


