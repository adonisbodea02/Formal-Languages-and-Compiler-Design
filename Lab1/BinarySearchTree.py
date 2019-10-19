class BinarySearchTree:

    def __init__(self):
        self.nodes = []

    def insert(self, value):
        if len(self.nodes) == 0:
            self.nodes.append(value)
            return 0
        else:
            position = 1
            inserted = False
            while position <= len(self.nodes) and inserted is False:
                if value < self.nodes[position-1]:
                    position *= 2
                    if position <= len(self.nodes):
                        if self.nodes[position-1] is None:
                            self.nodes[position-1] = value
                            inserted = True
                else:
                    position *= 2
                    position += 1
                    if position <= len(self.nodes):
                        if self.nodes[position-1] is None:
                            self.nodes[position-1] = value
                            inserted = True
            if not inserted:
                while len(self.nodes) < position:
                    self.nodes.append(None)
                self.nodes[len(self.nodes)-1] = value
            return position - 1

    def find(self, value):
        if len(self.nodes) == 0:
            return None
        else:
            position = 1
            while position <= len(self.nodes):
                if self.nodes[position-1] is None:
                    return None
                if value == self.nodes[position-1]:
                    return position - 1
                if value < self.nodes[position-1]:
                    position *= 2
                else:
                    position *= 2
                    position += 1
        return None


# b = BinarySearchTree()
# print(b.insert('cdf'))
# print(b.insert('abc'))
# b.insert('efg')
# b.insert('pl')
# b.insert('caa')
# print(b.insert('dcv'))
# b.insert('x')
# print(b.insert('mn'))
# b.insert('ca')
# print(b.nodes)
# print(b.find('mn'))



