import random

comparisonCounter = 0


def getComparisonCounterLinear():
    return comparisonCounter


class Empty: pass


class Deleted: pass


class Linear:

    def __init__(self, size):
        self.dictionary = {}
        for i in range(size):
            self.dictionary[i] = Empty

    def scan_for(self, value):
        global comparisonCounter
        comparisonCounter = 0
        firstIndex = hash(value) % len(self.dictionary)
        comparisonCounter += 1
        step = 1
        deletedIndex = -1
        index = firstIndex

        while self.dictionary[index] is not Empty:
            comparisonCounter += 1
            if self.dictionary[index] is Deleted:
                comparisonCounter += 1
                if deletedIndex == -1:
                    comparisonCounter += 1
                    deletedIndex = index
            elif self.dictionary[index] == value:
                comparisonCounter += 1
                return index
            index = (index + step) % len(self.dictionary)
            if index == firstIndex:
                comparisonCounter += 1
                return deletedIndex
        if deletedIndex != -1:
            comparisonCounter += 1
            return deletedIndex
        return index

    def find(self, value):
        index = self.scan_for(value)
        if index == -1 or self.dictionary[index] is Deleted or self.dictionary[index] is Empty:
            return None
        return self.dictionary[index]

    def insert(self, value):
        index = self.scan_for(value)
        if index == -1:
            raise IndexError
        self.dictionary[index] = value

    def delete(self, value):
        index = self.scan_for(self.dictionary[value])
        if index != -1 and index is not Empty:
            self.dictionary[index] = Deleted

    def print_table(self):
        print(self.dictionary)

    def insert_values(self, howMany, randomRangeA, randomRangeB):
        listOfNumbers = random.sample(range(randomRangeA, randomRangeB + 1), howMany)
        for i in listOfNumbers:
            self.insert(i)
