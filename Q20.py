# 函数和文件

from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # 转到文件对应的字节


def print_a_line(line_count, f):
    print(line_count, f.readline())


concurrent_file = open(input_file)

print("First let's print the whole file:\n")

print_all(concurrent_file)

print("Now let's rewind,kind of like a tape.")

rewind(concurrent_file)

print("let's print three lines:")

concurrent_line = 1
print_a_line(concurrent_line, concurrent_file)

concurrent_line = concurrent_line + 1
print_a_line(concurrent_line, concurrent_file)

concurrent_line = concurrent_line + 1
print_a_line(concurrent_line, concurrent_file)
