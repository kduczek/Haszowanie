import random


class Chain:

    def __init__(self, size):
        self.listOfLists = [[] for _ in range(size)]

    def find_index(self, value):
        h = hash(value) % len(self.listOfLists)
        for i in range(0, len(self.listOfLists[h])):
            if self.listOfLists[h][i] == value:
                return h, i
        return h, -1

    def find(self, value):
        (h, i) = self.find_index(value)
        if i == -1:
            return None
        return self.listOfLists[h][i]

    def insert(self, value):
        (h, i) = self.find_index(value)
        if i == -1:
            self.listOfLists[h].append(value)
        else:
            self.listOfLists[h][i] = value

    def delete(self, value):
        (h, i) = self.find(value)
        if i != -1:
            self.listOfLists[h][i].remove(value)

    def print_table(self):
        for i in self.listOfLists:
            print(i)

    def insert_values(self, howMany, randomRangeA, randomRangeB):
        for i in range(howMany):
            value = random.randint(randomRangeA, randomRangeB)
            while self.find_index(value)[1] != -1:
                value = random.randint(randomRangeA, randomRangeB)
            self.insert(value)


