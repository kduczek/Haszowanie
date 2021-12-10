import random

comparisonCounter = 0


def getComparisonCounter():
    return comparisonCounter


class Chain:

    def __init__(self, size):
        self.listOfLists = [[] for _ in range(size)]

    def find_index(self, value):
        global comparisonCounter
        comparisonCounter = 0
        hashValue = hash(value) % len(self.listOfLists)
        for index in range(0, len(self.listOfLists[hashValue])):
            comparisonCounter += 1
            if self.listOfLists[hashValue][index] == value:
                return hashValue, index
        return hashValue, -1

    def find(self, value):
        (hashValue, index) = self.find_index(value)
        if index == -1:
            return None
        return self.listOfLists[hashValue][index]

    def insert(self, value):
        (hashValue, index) = self.find_index(value)
        if index == -1:
            self.listOfLists[hashValue].append(value)
        else:
            self.listOfLists[hashValue][index] = value

    def delete(self, value):
        (hashValue, index) = self.find_index(value)
        if index != -1:
            self.listOfLists[hashValue].remove(value)

    def print_table(self):
        for index in self.listOfLists:
            print(index)

    def insert_values(self, howMany, randomRangeA, randomRangeB):
        for _ in range(howMany):
            value = random.randint(randomRangeA, randomRangeB)
            while self.find_index(value)[1] != -1:
                value = random.randint(randomRangeA, randomRangeB)
            self.insert(value)
