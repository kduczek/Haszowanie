import random

import matplotlib.pyplot as plt
from linear import Linear, getComparisonCounterLinear
from chain import Chain, getComparisonCounter


def printChartChainMethod():
    dictionaryChain = Chain(10000)
    X = []
    Y = []

    for i in range(100000):
        valueToAdd = random.randint(1, 200000)
        while dictionaryChain.find_index(valueToAdd)[1] != -1:
            valueToAdd = random.randint(1, 200000)
        dictionaryChain.insert(valueToAdd)
        X.append(i)
        Y.append(getComparisonCounter())

    plt.plot(X, Y)
    plt.xlabel("Ilość liczb w słowniku")
    plt.ylabel("Ilość porównań")
    plt.suptitle("Wykres zależności ilości porównań od ilości liczb w słowniku\n w łańcuchowej metodzie rozwiązywania "
                 "kolizji")
    plt.show()


def printChartLinearMethod():
    dictionaryLinear = Linear(100000)
    X = []
    Y = []

    for i in range(100000):
        valueToAdd = random.randint(1, 200000)
        while dictionaryLinear.find(valueToAdd) is None:
            valueToAdd = random.randint(1, 200000)
            dictionaryLinear.insert(valueToAdd)
        X.append(i)
        Y.append(getComparisonCounterLinear())

    plt.plot(X, Y)
    plt.xlabel("Ilość liczb w słowniku")
    plt.ylabel("Ilość porównań")
    plt.suptitle("Wykres zależności ilości porównań od ilości liczb w słowniku\n w liniowej metodzie rozwiązywania "
                 "kolizji")
    plt.show()


def linearTest():
    print("Linear TEST")
    linearMethod = Linear(30)
    linearMethod.insert_values(30, 1, 60)
    linearMethod.print_table()
    linearMethod.delete(21)
    linearMethod.delete(17)
    linearMethod.delete(3)
    linearMethod.print_table()
    print(linearMethod.find(13))
    print(linearMethod.find(19))
    print(linearMethod.find(59))


def chainTest():
    print("Chain TEST")
    chainMethod = Chain(30)
    chainMethod.insert_values(30, 1, 60)
    chainMethod.print_table()
    chainMethod.delete(21)
    chainMethod.delete(17)
    chainMethod.delete(3)
    print("After delete operation")
    chainMethod.print_table()
    print(chainMethod.find(13))
    print(chainMethod.find(19))
    print(chainMethod.find(59))
