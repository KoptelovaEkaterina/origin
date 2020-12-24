def insertion_sort(data, comparator):
    n = len(data)
    for i in range(1, n):
        k = data[i]
        index = i-1
        while index >= 0 and comparator(data[index], k) > 0:
            data[index + 1] = data[index]
            index -= 1
        data[index + 1] = k

def sort_seq(l, r):
    
    def dist(left, right):
        count = 0
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]:
                count += 1
        return count + max(len(left), len(right)) - min(len(left), len(right))
    
    def compare_seq(s1, s2):
        return dist(s1._data, r) - dist(s2._data, r)
    insertion_sort(l, compare_seq)