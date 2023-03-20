# 命名 变量 代码 函数
# this one is like your scripts with argv

def print_two(*args):  # 不定量参数
    print(type(args))
    arg1, arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1:{arg1},arg2:{arg2}")


def print_one(arg1):
    print(f"arg1:{arg1}")


def print_none():
    print("I got nothin .")


def print_key_word_args(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)


print_two("1", "2")
print_two_again("zed", "Shaw")
print_one("First")
print_none()
print_key_word_args(a="a", b=1)
