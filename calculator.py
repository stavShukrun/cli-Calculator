import sys
from typing import Counter

class Calculator():

    def take_expresion(self):
        try: 
            with open(sys.argv[1], 'r') as f:
                eqesioin = f.read()
        except IndexError:
            print('file is not exsist')
            print("write your expression:")
            eqesioin = input("> ")
        return eqesioin

    def calculate(self,eqesioin):
        arr = []
        for c in eqesioin:
            arr.append(c)
        return self.solver(arr)
    
    def solver(self, cal):
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        while len(cal) > 0:
            c = cal.pop(0)
            if c.isdigit():
                num = num*10+int(c)
            if len(cal) == 0 or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
                if sign == ')':
                    break
        return sum(stack)
    
cal= Calculator()
s=cal.take_expresion()
print(cal.calculate(s))
