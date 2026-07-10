class MinStack:

    def __init__(self):
        self.container = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.container.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        if self.minstack[-1] == self.container[-1]:
            self.minstack.pop()
        self.container.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
