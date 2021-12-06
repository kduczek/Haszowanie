import random


def hash_and_insert_into_table(element, dictionary):
    dictionary[hash(element) % 50].append(element)


def print_table(table):
    for index in table:
        print(index)


def initialize_list(size):
    dictionary = [[] for _ in range(size)]
    return dictionary


def find_element(element):
    return element in myDict[hash(element) % len(myDict)]


myDict = initialize_list(50)
for i in range(1, 100):
    hash_and_insert_into_table(random.randint(1, 100), myDict)

print_table(myDict)
print(find_element(27))
print(find_element(98))
print(find_element(13))
