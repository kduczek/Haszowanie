class Empty: pass


class Deleted: pass


class Linear:

    def __init__(self, size):
        self.dictionary = {}
        for i in range(size):
            self.dictionary[i] = Empty

    def scan_for(self, value):
        firstIndex = hash(value) % len(self.dictionary)
        step = 1
        deletedIndex = -1
        index = firstIndex

        while self.dictionary[index] is not Empty:
            if self.dictionary[index] is Deleted:
                if deletedIndex == -1:
                    deletedIndex = index
            elif self.dictionary[index] == value:
                return index
            index = (index + step) % len(self.dictionary)
            if index == firstIndex:
                return deletedIndex
        if deletedIndex != -1:
            return deletedIndex
        return index

    def find(self, value):
        index = self.scan_for(value)
        if index == -1 or index is Deleted or index is Empty:
            return None
        return self.dictionary[index]

    def insert(self, value):
        index = self.scan_for(value)
        if index == -1:
            raise IndexError
        self.dictionary[index] = value
