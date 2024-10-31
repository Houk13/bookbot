def main():
    book_path = "books/frankenstein.txt"
    get_report(book_path)
    

def get_report(book_path):
    text = get_book_text(book_path)
    nWords = get_num_words(text)
    chCount = get_num_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{nWords} words found in the document\n")
    for ch in chCount:
        print(f"The '{ch}' character was found {chCount[ch]} times")
    print("--- End report ---")

def get_num_chars(text):
    charCount = {}
    lowText = text.lower()
    for ch in lowText:
        if ch in charCount:
            charCount[ch] += 1
        else:
            charCount[ch] = 1
            print("new char: " + ch)

    return charCount

def get_num_words(text):
    return len(text.split())

def get_book_text(book_path):
    with open(book_path) as bookfile:
        return bookfile.read()


main()