import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNCTUATION = [",", "?", "!", ".", "'", '"']


def read_file(file):
    """Uses open to read a file

    Args:
        file (file ): A file to be read
    """
    with open(file) as opened_file:
        return opened_file.read()


def remove_punctuation(s):
    for punc in PUNCTUATION:
        s = s.replace(punc, "")
    return s


def remove_stop_words(s):
    for word in STOP_WORDS:
        if word in s:
            s = s.replace(f'/b{word}/b', "")
    return s

# def remove_stop_words(s):
#     list = s.split()
#     return_list = []
#     for word in list:
#         if word not in STOP_WORDS:
#             return_list.append(word)
#     return " ".join(return_list)


def print_word_freq(file):
    """Performs word frequency operations

    Args:
        file (string): A file to be read
    """
    file_read = read_file(file)
    # print(file_read)
    stripped_file = remove_punctuation(file_read).lower()
    cleaned_file = remove_stop_words(stripped_file)
    print(cleaned_file)
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
