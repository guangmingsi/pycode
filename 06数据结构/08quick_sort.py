def quick_sort(alist,first_pos,end_pos):
    #n = len(alist)
    if first_pos >= end_pos:
        return
    low =first_pos
    hight = end_pos
    min_value = alist[first_pos]

    while low < hight:
        while low < hight:
            if alist[hight] <  min_value:
                alist[low] = alist[hight]
                break
            else:
                hight -= 1


        while low <hight:
            if alist[low] >= min_value:
                alist[hight] = alist[low]
                break
            else:
                low += 1

    alist[low] = min_value
    quick_sort(alist,first_pos,pos-1)#这个函数进去后会调用quick（0.5）quick（3.5）然后退出

    quick_sort(alist,pos+1,end_pos)# 上面的函数执行完这个函数进去嵌套
if __name__ == "__main__":
    li = [23,4,5,19,67,45,18,17,15,565,77]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)