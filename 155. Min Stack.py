class Node:
    def __init__(self, value, min_value, old_top=None) -> None:
        self.value = value 
        self.min = min_value
        self.down: Node = old_top

class MinStack:

    def __init__(self):
        self._top = None

    def push(self, val: int) -> None:
        if not self._top:
            self._top = Node(val, val)
        else:
            self._top = Node(val, min(self._top.min, val), self._top)

    def pop(self) -> None:
        self._top = self._top.down

    def top(self) -> int:
        return self._top.value

    def getMin(self) -> int:
        return self._top.min


# list solution

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(3)
# print(obj.top())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()