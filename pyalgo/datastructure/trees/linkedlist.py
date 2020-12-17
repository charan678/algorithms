class Cell:
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedList:
    def __init__(self, value):
        self._start = Cell(value)

    @property
    def start(self):
        return self._start

    def delete(self, value):
        found = False
        start_node = self._start
        previous = None
        while start_node.value != value:
            previous = start_node
            start_node = start_node.link
        if not previous:
            self._start = self._start.link
        else:
            previous.link = start_node.link

    def add(self, value):
        start_node = self.start
        while start_node.link:
            start_node = start_node.link
        start_node.link = Cell(value)

    def traverse(self):
        start_node = self._start
        while start_node:
            print(start_node.value)
            start_node = start_node.link

if __name__  == "__main__":
    list_linked = LinkedList(10)
    list_linked.add(20)
    list_linked.add(30)
    list_linked.add(40)
    list_linked.traverse()
    print("-"*40)
    list_linked.delete(40)
    list_linked.traverse()
    print("-"*40)