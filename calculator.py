import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default= None ,help = "equation file")
    args = parser.parse_args()
    return args


def take_expresion(file_name) -> str:
    try: 
        with open(file_name,'r') as f:
            return f.read()

    except (FileNotFoundError, TypeError) :
        print('file is not exsist')
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
                
            else:
                raise SyntaxError(f"{c} is not legal")

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


def start_calculator():
    args = create_parser()
    salusion=take_expresion(args.f)
    cal= Calculator()
    print(cal.calculate(salusion))

if __name__ == '__main__':
    start_calculator()