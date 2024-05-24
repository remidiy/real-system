from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+':
                s.append(s.pop() + s.pop())
            elif t == '*':
                s.append(s.pop() * s.pop())
            elif t == '-':
                a1, a2 = s.pop(), s.pop()
                s.append(a2 - a1)
            elif t == '/':
                a1, a2 = s.pop(), s.pop()
                s.append(int(a2/a1))
            else:
                s.append(int(t))

            print(s)

        return s[0]
    
if __name__ == "__main__":
    s = Solution()
    # print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    a = [4,4,4,5,6]
    print(a[2:5])