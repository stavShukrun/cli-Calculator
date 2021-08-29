import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default= None ,help = "equation file")
    args = parser.parse_args()
    return args

def take_expresion(file_name: str) -> str:
    try: 
        with open(file_name,'r') as f:
            return f.read()

    except (FileNotFoundError, TypeError) :
        print('file is not exsist')
        print("write your expression:")
        equation = input("> ") 
        return equation

def count_calls(operation):
    def _counting(*args, **kwargs):
        _counting.count_operation += 1
        return operation(*args, **kwargs)
    _counting.count_operation = 0
    return _counting

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

    @count_calls
    def add(self,a: float,b: float) -> float:
        a+=b
        return a    

    @count_calls
    def subtract(self,a: float,b: float) -> float:
        a+=b
        return a    

    @count_calls
    def multiply(self,a: float,b: float) -> float:
        a=a*b
        return a

    @count_calls
    def divide(self,a: float,b: float) -> float:
        if(b==0):
            raise ZeroDivisionError("can't divided by zero")
        a=a/b
        return a

def start_calculator():
    args = create_parser()
    salusion=take_expresion(args.f)
    cal= Calculator()
    print(cal.calculate(salusion))
    print(f" Total operations: {cal.add.count_operation + cal.subtract.count_operation + cal.multiply.count_operation + cal.divide.count_operation} \n Add operations: {cal.add.count_operation} \n Subtract operations: {cal.subtract.count_operation} \n Multiply operations: {cal.multiply.count_operation} \n Divide operations: {cal.divide.count_operation} \n") # pylint: disable=no-member

if __name__ == '__main__':
    start_calculator()