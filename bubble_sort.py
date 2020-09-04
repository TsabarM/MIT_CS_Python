def bubble_sort(L):
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

if __name__ == "__main__":
    L = [5,4,38,2,85,25,4,6,2,8,2]
    print ('original list: ' + str(L))
    bubble_sort(L)
    print(L)
    