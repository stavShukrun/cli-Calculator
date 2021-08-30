import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default= None ,help = "equation file")
    args = parser.parse_args()
    return args

def take_expresions(file_name) -> str:
    try: 
        with open(file_name,'r') as f:
            lines = f.readlines()
            for equations in lines:
                yield equations

    except (FileNotFoundError, TypeError) :
        print('file is not exsist')
        print("write your expression:")
        equations = input("> ") 
        yield equations

    
class Calculator():

    def calculate(self,equation: str) -> float:
        equation_list = []
        for c in equation:
            equation_list.append(c)
        return self.solver(equation_list)
    
    def solver(self, pre_calculate_list: list)-> float:

        if len(pre_calculate_list) == 0:
            return 0

        stack = []
        sign = '+'
        num = 0
        decimals =0

        while len(pre_calculate_list) > 0:
            c = pre_calculate_list.pop(0)

            if c.isdigit() and sign != '.':
                num = num*10+float(c)

            if c.isdigit() and sign == '.':
                decimals +=1
                num += (float(c))*(0.10**decimals)

            if len(pre_calculate_list) == 0 or (c == '+' or c == '-' or c == '*' or c == '/' or c == '.'):
                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack[-1] = self.multiply(stack[-1],num)

                elif sign == '/':
                    stack[-1] = self.divide(stack[-1],num)

                elif sign == '.':
                    stack.append(num)

                decimals =0
                sign = c
                num = 0
        return self.sum(stack)


    def sum(self,stack: list) -> float:
        if len(stack)==1:
            return stack[0]

        sum = stack[0]
        for num in range(len(stack)-1):
            if stack[num+1] > 0:
                sum = self.add(sum,stack[num+1])
            elif stack[num+1] < 0:
                sum = self.subtract(sum,stack[num+1])
        return sum


    def add(self,a: float,b: float) -> float:
        a+=b
        return a    
    

    def subtract(self,a: float,b: float) -> float:
        a+=b
        return a    


    def multiply(self,a: float,b: float) -> float:
        a=a*b
        return a


    def divide(self,a: float,b: float) -> float:
        if(b==0):
            raise ZeroDivisionError("can't divided by zero")
        a=a/b
        return a

def start_calculator():
    args = create_parser()
    salusions=take_expresions(args.f)
    cal= Calculator()
    for s in salusions:
        print(cal.calculate(s))

if __name__ == '__main__':
    start_calculator()