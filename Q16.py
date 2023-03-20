from sys import argv

"""
close: 关闭文件
read: 读取文件的内容
readline: 只读取文件中的一行
truncate: 清空文件
write('stuff'): 将stuff 写入文件
seek(0): 将读取位置移到文件开头
"""
scrip, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that , hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")  # w+:读写 r+:文件必须存在 a+:读写

print("Truncating the file.Goodbye!")
target.truncate()

print("Now I'm going tp write these to the file.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it.")
target.close()
