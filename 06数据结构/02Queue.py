class Queue(object):
    def __init__(self):
        """Queue() 创建一个空的队列"""
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个item元素"""
        # 列表尾部为队列头部
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        # 列表尾部是队列头部，出队就要从列表头部出
        if self.__list == []:
            return
        else:
            return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

if __name__ == "__main__":
    queue = Queue()
    print(queue.dequeue())
    print(queue.is_empty())
    queue.enqueue(1)
    print(queue.size())
    print(queue.dequeue())
