from pyalgo.algo.sorting.heap import MinHeap, MaxHeap

min_heap = MinHeap()
max_heap = MaxHeap()

def runningMedian(a):

    if len(min_heap.heap_list) == 0 or len(max_heap.heap_list) == 0:
        max_heap.add_value(a)
        return max_heap.heap_list[0]
    else:
        if a < max_heap.heap_list[0]:
            min_heap.add_value(a)
        else:
            pass

    if (len(min_heap.heap_list) + len(max_heap.heap_list))%2 ==0:
        return max_heap.heap_list[:-1]
    else:
        return (max_heap.heap_list[:-1] + min_heap.heap_list[0])/2

if __name__ == "__main__":

    assert(runningMedian(12) == 12)
