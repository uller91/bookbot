def main():
    path = "books/frankenstein.txt"
    file_contents = open_file(path)
    count_words = word_count(file_contents)
    count_characters = characters_count(file_contents)
    divided_dict = divide_dict(count_characters)
    divided_dict.sort(reverse=True, key = sort_on)
    report(path, count_words, divided_dict)
    

def report(path, words, list):    
    print(f"--- Begin report of {path} ---\n"
        f"{words} words was found in this document\n")
    for dict in list:
        print(f"The '{dict["letter"]}' character was found {dict["number"]} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["number"]


def divide_dict(dict):
    list_of_letters = []
    for key in dict:
        list_of_letters.append({"letter" : key, "number" : dict[key]})
    return list_of_letters


def characters_count(text):
    lower_text = text.lower()   #in the solution it is done within the for loop
    dictionary = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in dictionary.keys():
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary


def word_count(text):
    split_text = text.split()
    return len(split_text)


def open_file(path):
    with open(path) as f:
        return f.read()


main()