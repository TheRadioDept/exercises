def words_count():
    """
    Count number of words in "poem.txt"
    """
    file = open("poem.txt", "r")
    data = file.read()
    words = data.split()
    print("Number of words is {0}".format(len(words)))
    file.close()


def non_empty_line_count():
    """
    Count numbers of Non-empty lines in "poem.txt"
    """
    file = open("poem.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    print("Number of non empty lines is {0}".format(line_count))
    file.close()


def char_count():
    """
    Count number of characters in "poem.txt"
    """
    file = open("poem.txt", "r")
    data = file.read().replace(" ", "")
    number_of_characters = len(data)

    print("Number of characters in text file is {0}".format(number_of_characters))
    file.close()
