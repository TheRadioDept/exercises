def count_words(ignore_whitespace=False):
    """
    Count number of words in "poem.txt"
    """
    file = open("poem.txt", "r")
    data = file.read()
    words = data.split()
    print("Number of words: {0}".format(len(words)))
    file.close()


def count_lines(ignore_whitespace=False):
    """
    Count numbers of Non-empty lines in "poem.txt"
    """
    file = open("poem.txt", "r")
    line_count = 0
    for line in file:
        if ignore_whitespace:
            if line != "\n":
                line_count += 1
        else:
            line_count += 1

    print("Number of lines: {0}".format(line_count))
    file.close()


def count_characters(ignore_whitespace=False):
    """
    Count number of characters in "poem.txt"
    """
    file = open("poem.txt", "r")
    number_of_characters = 0
    for line in file:
        if ignore_whitespace:
            line = line.strip("\n")
            number_of_characters += len(line)
        else:
            number_of_characters += len(line)

    print("Number of chars: {0}".format(number_of_characters))
    file.close()
