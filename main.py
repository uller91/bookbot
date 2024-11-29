def main():
    file_contents = open_file("books/frankenstein.txt")
    count = word_count(file_contents)
    print(f"{count} words was found in this document")




def word_count(text):
    split_text = text.split()
    return len(split_text)


def open_file(path):
    with open(path) as f:
        return f.read()


main()