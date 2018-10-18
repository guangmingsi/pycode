def merge_sort(alist):
    # 递归停止语句

    n = len(alist)
    if n <=1:
        return alist
    mid_ver = n//2
    #递归函数，先分解到最小
    left_li = merge_sort(alist[0:mid_ver])
    right_li = merge_sort(alist[mid_ver:])
    # 左指针和右指针
    left_pointer,right_pointer = 0,0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    #添加最后一个元素，但是不确定在哪边所以都写下不影响
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__ == "__main__":
    li = [23,4,5,19,67,45,18,17,15,565,77]
    print(li)
    srotli = merge_sort(li)
    print(srotli)