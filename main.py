def main():
    file_contents = open_file("books/frankenstein.txt")     #in the solution the path is a variable
    count_words = word_count(file_contents)
    print(f"{count_words} words was found in this document")
    count_characters = characters_count(file_contents)
    print(count_characters)



def characters_count(text):
    lower_text = text.lower()   #in the solution it is done within the for loop
    dictionary = {}
    for letter in lower_text:
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