class VirtualMachine:
    def __init__(self, quadruples, global_vars, functions):
        self.quadruples = quadruples
        self.global_vars = global_vars
        self.functions = functions
        self.temp_vars = {}
        self.instruction_pointer = 0
        self.call_stack = []

    def run(self):
        try:
            while self.instruction_pointer < len(self.quadruples):
                quad = self.quadruples[self.instruction_pointer]
                self.execute_quad(quad)
                self.instruction_pointer += 1
        except Exception as e:
            print(f"Runtime error: {e}")

    def execute_quad(self, quad):
        op, arg1, arg2, result = quad
        if op == '*':
            self.temp_vars[result] = self.get_value(arg1) * self.get_value(arg2)
        elif op == '/':
            divisor = self.get_value(arg2)
            if divisor == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            self.temp_vars[result] = self.get_value(arg1) / divisor
        elif op == '+':
            self.temp_vars[result] = self.get_value(arg1) + self.get_value(arg2)
        elif op == '-':
            self.temp_vars[result] = self.get_value(arg1) - self.get_value(arg2)
        # ... handle other operations
        elif op == 'PRINT':
            print(self.get_value(arg1))
        # ... handle other operations

    def get_value(self, operand):
        if isinstance(operand, (int, float)):
            return operand
        elif isinstance(operand, str) and operand.isdigit():
            return int(operand)
        elif isinstance(operand, str) and self.is_float(operand):
            return float(operand)
        elif operand in self.temp_vars:
            return self.temp_vars[operand]
        elif operand in self.global_vars:
            return self.global_vars[operand]['value']
        else:
            raise ValueError(f"Invalid operand: {operand}")

    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

# Example usage:
quadruples = [
    ('*', '2', '3', 't1'),
    ('/', 't1', '1', 't2'),  # This will cause a division by zero error
    ('+', 't1', '5', 't3'),
    ('PRINT', 't3', None, None),
]

global_vars = {
    'x': {'value': 10},
    'y': {'value': 20},
}

functions = {}

vm = VirtualMachine(quadruples, global_vars, functions)
vm.run()