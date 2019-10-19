from BinarySearchTree import BinarySearchTree


class SymbolTable:
    def __init__(self):
        self.__binarySearchTree = BinarySearchTree()

    def insert(self, value):
        return self.__binarySearchTree.insert(value)

    def find(self, value):
        return self.__binarySearchTree.find(value)

    def __str__(self):
        s = 'Symbol Table:\n'
        for i in range(len(self.__binarySearchTree.nodes)):
            if self.__binarySearchTree.nodes[i] is not None:
                s += str(i) + ' ' + self.__binarySearchTree.nodes[i] + '\n'
        return s
