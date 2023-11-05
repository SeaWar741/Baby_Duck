from collections import deque

class SemanticAnalyzer:
    ERROR = "ERROR"
    
    def __init__(self):
        # Semantic cube
        self.Semantics = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '*': 'int',
                    '/': 'int'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                }
            },
            'float': {
                'int': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float'
                }
            }
        }
        
        # Stacks for control structures
        self.OperandStack = []  # Stack for operands
        self.TypeStack = []     # Stack for types
        self.OperatorStack = [] # Stack for operators
        self.JumpStack = []     # Stack for jumps (for control structures like if, while, etc.)

        # Queue for quadruples
        self.Quadruples = deque()  # Queue for quadruples

        # Available memory for temporary results
        self.AVAIL = {"next": 1000}
    
    def generate_quad(self, operator, left_operand, right_operand):
        result = self.AVAIL["next"]
        self.AVAIL["next"] += 1
        quad = (operator, left_operand, right_operand, result)
        self.Quadruples.append(quad)
        return result
    
    def process_operation(self, operators):
        if self.OperatorStack and self.OperatorStack[-1] in operators:
            right_operand = self.OperandStack.pop()
            right_type = self.TypeStack.pop()
            left_operand = self.OperandStack.pop()
            left_type = self.TypeStack.pop()
            operator = self.OperatorStack.pop()
            
            result_type = self.Semantics[left_type][right_type].get(operator, self.ERROR)
            if result_type != self.ERROR:
                result = self.generate_quad(operator, left_operand, right_operand)
                self.OperandStack.append(result)
                self.TypeStack.append(result_type)
            else:
                raise Exception("Type mismatch")
    
    # Additional methods for managing the stacks and queue
    def push_operator(self, operator):
        self.OperatorStack.append(operator)

    def push_operand(self, operand):
        self.OperandStack.append(operand)

    def push_type(self, type):
        self.TypeStack.append(type)

    def push_jump(self, jump):
        self.JumpStack.append(jump)

    def pop_jump(self):
        return self.JumpStack.pop() if self.JumpStack else None

    def enqueue_quad(self, quad):
        self.Quadruples.append(quad)

    def dequeue_quad(self):
        return self.Quadruples.popleft() if self.Quadruples else None
    
    def get_type(self, operand):
        if operand.isdigit():
            return "int"
        elif operand.replace('.', '', 1).isdigit():
            return "float"
        else:
            return "unknown"
    def is_operation(self, operand):
        return operand in ['+', '-', '*', '/']


""" analyzer = SemanticAnalyzer()

analyzer.push_operand("variable1")
analyzer.push_type("int")
analyzer.push_operator("+")

analyzer.push_operand("variable2")
analyzer.push_type("float")

analyzer.process_operation(['+', '-'])

# Print the generated quadruples
while analyzer.Quadruples:
    print(analyzer.dequeue_quad())
 """