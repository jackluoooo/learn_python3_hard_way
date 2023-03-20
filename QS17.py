from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}')

in_file = open(from_file)
in_data = in_file.read()
print(in_data)

print(f"The input file is {len(in_data)} byte long")

print(f"Does the output file exist?{exists(to_file)}")

input("准备好了吗？")

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright , all done")

out_file.close()
in_file.close()
