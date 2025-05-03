
def get_book_text(book_path):

    with open(book_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def main():
    print(get_book_text('~/bookbot/books/frankenstein.txt'))

main()