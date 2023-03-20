# 更多的联系
print("Let's practice everything.")
print('You\' need to know \'bout escapes with \\ that do:')

poem = """
\t the lovely world
"""

print(poem)

five = 10 - 2 + 3 - 6
print(f"This should be five :{five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print(f"With a starting point of:{start_point}")
print(f"We'd have {beans} beans,{jars} jars,add {crates} creates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print("We'd have {} beans,{} jars, and {} crates.".format(*formula))
