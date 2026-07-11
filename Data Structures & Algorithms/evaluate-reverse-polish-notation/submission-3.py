class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        container = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:

                container.append(int(t))
            else:
                a = container.pop()
                b = container.pop()
                if t == '+':
                    container.append(a+b)
                elif t == '-':
                    container.append(b-a)                  
                elif t == '*':
                    container.append(a*b)                  
                elif t == '/':
                    container.append(int(b/a))   
        return container[0]               