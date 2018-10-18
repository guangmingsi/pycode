def bubble_sort(list):
    n = len(list)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if list[i]> list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                count += 1
        if count == 0:
            return
if __name__ == "__main__":
    li = [1,4,5,3,2,19,2,45,11]
    print(li)
    bubble_sort(li)
    print(li)