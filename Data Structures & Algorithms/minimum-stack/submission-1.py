class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s = []
        

    def push(self, val: int) -> None:
        n = len(self.stack)
        if n:
            self.min_s.append(min(self.min_s[-1], val))
        else:
            self.min_s.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_s.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        
