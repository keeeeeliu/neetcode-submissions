class LinkedList:
    
    def __init__(self):
        self.array = []
        self.size = 0

    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.array[index]
        

    def insertHead(self, val: int) -> None:
        self.array.append(0)
        for i in range(len(self.array)-1, 0, -1):
            self.array[i] = self.array[i-1]
        self.array[0] = val
        self.size += 1

    def insertTail(self, val: int) -> None:
        self.array.append(val)
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]

        self.array.pop()
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        return self.array[:len(self.array)]
