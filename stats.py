def get_num_words(text):

    num_words = len(text.split())
  
    return num_words

def sort_on(dict):
    return dict["num"]

def count_letters(text):

    num_letters = 0
    text = text.lower()

    dict =[
        {"char": "a", "num": 0},
        {"char": "b", "num": 0},
        {"char": "c", "num": 0},
        {"char": "d", "num": 0},
        {"char": "e", "num": 0},
        {"char": "f", "num": 0},
        {"char": "g", "num": 0},
        {"char": "h", "num": 0},
        {"char": "i", "num": 0},
        {"char": "j", "num": 0},
        {"char": "k", "num": 0},
        {"char": "l", "num": 0},
        {"char": "m", "num": 0},
        {"char": "n", "num": 0},
        {"char": "o", "num": 0},
        {"char": "p", "num": 0},
        {"char": "q", "num": 0},
        {"char": "r", "num": 0},
        {"char": "s", "num": 0},
        {"char": "t", "num": 0},
        {"char": "u", "num": 0},
        {"char": "v", "num": 0},
        {"char": "w", "num": 0},
        {"char": "x", "num": 0},
        {"char": "y", "num": 0},
        {"char": "z", "num": 0},
        {"char": ".", "num": 0},
        {"char": ",", "num": 0},
        {"char": "!", "num": 0},
        {"char": "?", "num": 0},
        {"char": ":", "num": 0},
        {"char": ";", "num": 0},
        {"char": "(", "num": 0},
        {"char": ")", "num": 0},
        {"char": '"', "num": 0},
        {"char": "'", "num": 0},
        {"char": "-", "num": 0},
        {"char": "_", "num": 0},
        {"char": "0", "num": 0},
        {"char": "1", "num": 0},
        {"char": "2", "num": 0},
        {"char": "3", "num": 0},
        {"char": "4", "num": 0},
        {"char": "5", "num": 0},
        {"char": "6", "num": 0},
        {"char": "7", "num": 0},
        {"char": "8", "num": 0},
        {"char": "9", "num": 0}
    ]



    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            for entry in dict:
                if entry["char"] == char:
                    entry["num"] += 1
                    break

    dict.sort(reverse=True, key=sort_on)



    for entry in dict:
        if entry["num"] > 0:
            print(f"{entry['char']}: {entry['num']}")



