def inser_sort(alist):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break
if __name__ == "__main__":
    li = [1,4,5,3,2,19,2,45,11]
    print(li)
    inser_sort(li)
    print(li)