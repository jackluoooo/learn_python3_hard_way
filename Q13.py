# 参数解包和变量
from sys import argv

# read the WYSS section
script, first, second, third = argv

print("the script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
