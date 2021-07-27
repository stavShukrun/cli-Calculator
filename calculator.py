import sys
from typing import Counter


def count_calls(fn):
    def _counting(*args, **kwargs):
        _counting.calls += 1
        return fn(*args, **kwargs)
    _counting.calls = 0
    return _counting
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
        if len(cal) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        while len(cal) > 0:
            c = cal.pop(0)
            if c.isdigit():
                num = num*10+float(c)
            if len(cal) == 0 or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    print("+")
                    stack.append(num)
                elif sign == '-':
                    print("-")
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = self.multiply(stack[-1],num)
                elif sign == '/':
                    stack[-1] = self.divide(stack[-1],num)
                sign = c
                num = 0
        return sum(stack)
    
    def add(self,a,b):
        a=+b
        return a    
    
    @count_calls
    def multiply(self,a,b):
        a=a*b
        return a

    @count_calls
    def divide(self,a,b):
        if(b==0):
            raise ZeroDivisionError("can't divided by zero")
        a=a/b
        return a
    
cal= Calculator()
s=cal.take_expresion()
print(cal.calculate(s))
print(cal.divide.calls) # pylint: disable=no-member