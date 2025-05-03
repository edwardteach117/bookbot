from stats import get_num_words
from stats import count_letters
from stats import sort_on
import os
import sys
import argparse

def get_book_text(book_path):

    with open(book_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py frankenstein.txt")
        sys.exit(1)

    path = str(sys.argv[1])
    book_path = "/home/sam/bookbot/" + path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"=========BOOKBOT=========")
    print(f"Analyzing Book......")
    print(f"----------- Word Count -----------")
    print(f"Found {num_words} total words in the document")

    print(f"----------- Character Count -----------")

    text = get_book_text(book_path)
    count_letters(text)
    print(f"===========END===========\n")

    

main()