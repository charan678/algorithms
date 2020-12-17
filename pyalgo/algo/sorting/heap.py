class MinHeap:
    def __init__(self):
        self.heap_list = []

    def add_value(self, value):
        self.heap_list.append(value)

    def swap(self, from_index, to_index):
        temp = self.heap_list[from_index]
        self.heap_list[from_index] = self.heap_list[to_index]
        self.heap_list[to_index] = temp

    def heapify(self, end_index,  index):
        left_x = 2 * index + 1
        right_y = 2 * index + 2
        larger = self.heap_list[:end_index][index]
        larger_index = index
        if len(self.heap_list[:end_index]) - 1 >= left_x and self.heap_list[:end_index][left_x] > larger:
            larger = self.heap_list[:end_index][left_x]
            larger_index = left_x
        if len(self.heap_list[:end_index]) - 1  >= right_y and self.heap_list[:end_index][right_y] > larger:
            larger = self.heap_list[:end_index][right_y]
            larger_index = right_y

        if larger != self.heap_list[:end_index][index]:
            self.swap(index, larger_index)
            self.heapify(end_index, larger_index)

    def extraction(self):
        for index in range(len(self.heap_list) - 1, 0, -1):
            self.swap(0, index)
            self.heapify(index, 0)

    def build_heap(self):
        for index in range(len(self.heap_list)//2, -1, -1):
            self.heapify(len(self.heap_list)-1, index)

    def print(self):
        for val in self.heap_list:
            print(val, end="\t")

class MaxHeap:
    def __init__(self):
        self.heap_list = []

    def add_value(self, value):
        self.heap_list.append(value)

    def swap(self, from_index, to_index):
        temp = self.heap_list[from_index]
        self.heap_list[from_index] = self.heap_list[to_index]
        self.heap_list[to_index] = temp

    def heapify(self, end_index,  index):
        left_x = 2 * index + 1
        right_y = 2 * index + 2
        smaller = self.heap_list[:end_index][index]
        smaller_index = index
        if len(self.heap_list[:end_index]) - 1 >= left_x and self.heap_list[:end_index][left_x] < smaller:
            smaller = self.heap_list[:end_index][left_x]
            smaller_index = left_x
        if len(self.heap_list[:end_index]) - 1  >= right_y and self.heap_list[:end_index][right_y] < smaller:
            smaller = self.heap_list[:end_index][right_y]
            smaller_index = right_y

        if smaller != self.heap_list[:end_index][index]:
            self.swap(index, smaller_index)
            self.heapify(end_index, smaller_index)

    def extraction(self):
        for index in range(len(self.heap_list) - 1, 0, -1):
            self.swap(0, index)
            self.heapify(index, 0)

    def build_heap(self):
        for index in range(len(self.heap_list)//2, -1, -1):
            self.heapify(len(self.heap_list)-1, index)

    def print(self):
        for val in self.heap_list:
            print(val, end="\t")

if __name__ == "__main__":
    min_heap = MaxHeap()
    min_heap.add_value(10)
    min_heap.add_value(1)
    min_heap.add_value(18)
    min_heap.add_value(8)
    min_heap.add_value(11)
    min_heap.add_value(4)
    min_heap.add_value(2)
    min_heap.build_heap()
    min_heap.extraction()
    min_heap.print()
    print()
    print("--"*40)
    min_heap = MinHeap()
    min_heap.add_value(10)
    min_heap.add_value(1)
    min_heap.add_value(18)
    min_heap.add_value(8)
    min_heap.add_value(11)
    min_heap.add_value(4)
    min_heap.add_value(2)
    min_heap.build_heap()
    min_heap.extraction()
    min_heap.print()