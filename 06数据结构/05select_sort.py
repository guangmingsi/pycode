# 选择排序
def select_sort(list):
    n = len(list)
    # 最小游标位置遍历
    for i in range(0,n-1):
        # 筛选区循环，逐个递减应该
        min_cur = i
        # 筛选区游标,选出最小的元素
        for j in range(i+1,n):
            if list[min_cur] > list[j]:
                min_cur = j
      #          list[min_cur],list[j] = [j],list[min_cur]
        # 将最小的元素和要替换的元素交换位置
        list[i],list[min_cur] = list[min_cur],list[i]
if __name__ == "__main__":
    li = [1,4,5,3,2,19,2,45,11]
    print(li)
    select_sort(li)
    print(li)