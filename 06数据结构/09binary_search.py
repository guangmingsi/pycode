def binary_search(alist,item):
    # 二分查找就是每次都分一半，看看中间值是不是要找的，要是不是看是在左边还是在右边，在分一半查找
    n = len(alist)
    mid = n//2
    # 递归n<= 0时候结束
    if n >0:
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                # 在中间点左边
                return binary_search(alist[:mid],item)
            else:
                # 在中间点右边
                return binary_search(alist[mid+1:],item)
    return False
def binary_search1(alist,item):
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        # 找到情况
        if alist[mid] == item:
            return True
        # 在左边
        elif alist[mid] >item:
            last = mid -1
        else:
            first = mid +1
    return False
li = [19,34,123,342,544,652,666]
print(binary_search(li,888))
print(binary_search(li,342))
print(binary_search1(li,888))
print(binary_search1(li,544))