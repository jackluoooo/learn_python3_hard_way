# 更多的练习

def break_words(stuff):
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    print(type(words))
    word = words.pop(0)
    print(word)


def print_last_world(words):
    print(words.pop(-1))


def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_world(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_world(words)


sentence = "All good things come to those who wait."
words = break_words(sentence)
print(words)
sorted_words = sort_words(words)
print(sorted_words)
print_first_word(words)
print_last_world(words)
sorted_words = sort_sentence(sentence)
print(sorted_words)
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
