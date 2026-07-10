class Solution:
    def isValid(self, st: str) -> bool:

        container = []
        for s in st:
            if s == '(' or s == '{' or s == '[':
                container.append(s)
            else:
                if not container:
                    return False
                if s == ')':
                    if container[-1] == '(':
                        container.pop()
                    else:
                        return False
                elif s == '}':
                    if container[-1] == '{':
                        container.pop()
                    else:
                        return False   
                elif s == ']':
                    if container[-1] == '[':
                        container.pop()
                    else:
                        return False
        if not container:
            return True
        return False