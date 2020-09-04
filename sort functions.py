def bubble_sort(L):
    # O(n^2)
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selection_sort(L):
    # O(n^2)
    """
    find minimum and put it first, than look only from 
    the n-1 rest of the list and do the same.
    afer i step the i first elements are smallest and sorted.
    """
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

def merge(left, right):
    """
    split list to two list. sort each and merge them. 
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right))
    return result

def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)

if __name__ == "__main__":
    L = [5,4,38,2,85,25,4,6,2,8,2]
    print ('original list: ' + str(L))
    merge_sort(L)
    # bubble_sort(L)
    # print(L)
    