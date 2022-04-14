import string
import sys


def words_count():
    file = open("poem.txt", "r")
    data = file.read()
    words = data.split()
    print('Number of words is ' + str(len(words)))


def non_empty_line_count():
    file = open("poem.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    print('Number of non empty lines is : ' + str(line_count))


def char_count():
    file = open("poem.txt", "r")
    data = file.read().replace(" ", "")

    # get the length of the data
    number_of_characters = len(data)

    print('Number of characters in text file :' + str(number_of_characters))


if __name__ == '__main__':
    globals()[sys.argv[1]]()
