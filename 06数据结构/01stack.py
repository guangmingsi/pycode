class Stack(object):
    # 创建一个空栈
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶 列表开头当作栈底"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        # 判断栈是否为空
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []


    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == "__main__":
    stack = Stack()
    stack.is_empty()
    stack.push(1)
    print(stack.peek())
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.size()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())