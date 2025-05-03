from stats import get_num_words

def get_book_text(book_path):

    with open(book_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    text = get_book_text("/home/sam/bookbot/books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()