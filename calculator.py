import argparse
import time

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default= None ,help = "equation file")
    args = parser.parse_args()
    return args


def take_expresion(file_name: str) -> str:
    try: 
        with open(file_name,'r') as f:
            return f.read()

    except (FileNotFoundError):
        raise
    except (TypeError):
        print("write your expression:")
        equation = input("> ") 
        return equation


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
        sum = stack[0]
        for num in range(len(stack)-1):
            if stack[num+1] > 0:
                sum = self.add(sum,stack[num+1])
            elif stack[num+1] < 0:
                sum = self.subtract(sum,stack[num+1])
        return round(sum,round_val)


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

class Timer():
    def __init__(self) -> None:
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        print(f"Time needed: {elapsed_time:0.4f} seconds")

    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        self.stop()

def start_calculator():
    with Timer():
        args = create_parser()
        salusion=take_expresion(args.f)
        cal= Calculator()
        print(cal.calculate(salusion))

if __name__ == '__main__':
    start_calculator()