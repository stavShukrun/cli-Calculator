""" Main """
import argparse
import threading
import time

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default= None ,help = "equation file")
    args = parser.parse_args()
    return args


def take_expresions(file_name: str) -> str:
    try: 
        with open(file_name,'r') as f:
            lines = f.readlines()
            for equations in lines:
                yield equations

    # except (FileNotFoundError):
    #     raise FileNotFoundError("please check File")
    except (TypeError):
        print("write your expression:")
        equations = input("> ") 
        yield equations

def count_operations(operation):
    def _counting(*args, **kwargs):
        _counting.count_operation += 1
        return operation(*args, **kwargs)
    _counting.count_operation = 0
    return _counting

class Calculator():

    def calculate(self,equation: str) -> float:
        equation_list = list(equation)
        return self.solver(equation_list)
    

    def solver(self, pre_calculate_list: list)-> float:

        equation_length = len(pre_calculate_list)
        if equation_length == 0:
            raise IndexError('Empty File')

        stack =[]
        num=[]
        sign = '+'
        for c in pre_calculate_list:
            
            if (c.isdigit() or c=='.') and equation_length != 1:
                num.append(c)
            
            elif c.isalpha():
                raise SyntaxError(f"{c} is not legal")

            elif c == '+' or c == '-' or c == '*' or c == '/' or equation_length == 1:

                if equation_length == 1:
                    num.append(c)

                temp=''.join(num)

                if sign == '+':
                    stack.append(float(temp))

                elif sign == '-':
                    negative_num = float(temp)
                    stack.append(-negative_num)

                elif sign == '*':
                    stack[-1] = (self.multiply(float(stack[-1]),float(temp)))

                elif sign == '/':
                    stack[-1] = self.divide(float(stack[-1]),float(temp))
                
                sign = c
                num=[]

            equation_length -=1
        return self.sum(stack)

    def sum(self,stack: list) -> float:

        round_val = 4
        sum_in_stack = stack[0]
        for num in range(len(stack)-1):
            if stack[num+1] > 0:
                sum_in_stack = self.add(sum_in_stack,stack[num+1])
            elif stack[num+1] < 0:
                sum_in_stack = self.subtract(sum_in_stack,stack[num+1])
        return round(sum_in_stack,round_val)

    @count_operations
    def add(self,a: float,b: float) -> float:
        a+=b

        return a    

    @count_operations
    def subtract(self,a: float,b: float) -> float:
        a+=b
        return a    

    @count_operations
    def multiply(self,a: float,b: float) -> float:
        a=a*b
        return a

    @count_operations
    def divide(self,a: float,b: float) -> float:
        if(b==0):
            raise ZeroDivisionError("can't divided by zero")
        a=a/b
        return a

class BackgrundThreadAdditions(threading.Thread):
    """"Thread Class"""
    def __init__(self, interval:int =1) -> None:
        threading.Thread.__init__(self)
        self.interval = interval

    def run(self):
        cal = Calculator
        while True:
            number_of_addition =cal.add.count_operation
            print("background thread number of additions ",number_of_addition)
            time.sleep(self.interval)

def start_calculator():
    new_thread = BackgrundThreadAdditions()
    new_thread.start()
    cal= Calculator()
    args = create_parser()
    salusions=take_expresions(args.f)
    cal= Calculator()
    for s in salusions:
        print(cal.calculate(s))
    print(f"""    Total operations: {cal.add.count_operation + cal.subtract.count_operation + cal.multiply.count_operation + cal.divide.count_operation}
    Add operations: {cal.add.count_operation}
    Subtract operations: {cal.subtract.count_operation}
    Multiply operations: {cal.multiply.count_operation}
    Divide operations: {cal.divide.count_operation} """)

if __name__ == '__main__':
    start_calculator()