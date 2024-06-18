def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    format_output(book_path, num_words, num_chars)
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)
def get_num_chars(text):
    lowered_text = text.lower()
    alphabet = {}
    for char in lowered_text:
        if (char in alphabet):
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet
def format_output(path, num_words, num_chars):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("\n")
    alphabet = []
    for alpha in num_chars:
        if alpha.isalpha():
            alphabet.append({"letter": alpha, "num": num_chars[alpha]})
    alphabet.sort(reverse=True, key=sort_on)
    for beta in alphabet:
        print(f"The '{beta['letter']}' character was found {beta['num']} times")
    print("--- End report ---")
def sort_on(dict):
    return dict["num"]

main()
