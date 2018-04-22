import array_stack

stack = array_stack.ArrayStack()

# input_file = open("input.txt", "r")

input_file = "4 6 + 13 11 - / 3 *"
answer_list = []

numerical_vals = "1234567890"
valid_operators = "+  - * /"

def calculate(expression):
    hold = []
    reversed_hold = []
    exp = ""
    expression_list = expression.split()
    for value in expression_list:
        if value.isnumeric():
            
            stack.push(value)
        elif value in valid_operators:
            hold.append(stack.pop())
            hold.append(value)
            hold.append(stack.pop())
            for i in range(3):
                reversed_hold.append(hold.pop())
            exp = ''.join(reversed_hold)
            
            reversed_hold = []
            hold = []
            answer = eval(exp)
            stack.push(str(answer))
    return stack.top()


def main():
  
    print(calculate(input_file))

if __name__ == '__main__':
    main()