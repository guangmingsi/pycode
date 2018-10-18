def shell_sort(alist):
    n = len(alist)



    # 设定一个gap步长，一般取列表长度一般取余
    gap = n//2
    while gap >= 1:
        # 从步长gap的元素开始，向减一个步长的元素做插入排序
        for i in range(gap,n):
            # 和倒数第二个比完，继续比，直到和倒数第一个比完
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:
                    break



        gap = gap//2

if __name__ == "__main__":
    li = [23,4,5,3,2,19,2,45,11,18,17,15,565]
    print(li)
    shell_sort(li)
    print(li)