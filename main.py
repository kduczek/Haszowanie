import random

from chain import Chain

test = Chain(50)
for i in range(1, 100):
    test.insert(random.randint(1, 100))

test.print_table()
