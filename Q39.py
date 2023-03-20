# 字典操作
things = ["1", "2", "3", "4"]
print(things[1])
things[1] = 'z'
print(things)

# dict eg:

states = {
    'Oregon': "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

cities['NY'] = "Mew York"
cities['OR'] = 'Portland'

# print out some cities
print("-" * 10)
