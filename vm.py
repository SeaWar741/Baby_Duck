class VirtualMachine:
    def __init__(self, quadruples, global_vars, functions):
        self.quadruples = quadruples
        self.global_vars = global_vars
        self.functions = functions
        self.temp_vars = {}
        self.instruction_pointer = 0
        self.call_stack = []
        self.temp_base_address = 2000
        self.temp_counter = 0
        self.temp_to_memory = {}

    def run(self):
        self.map_temporaries()
        try:
            while self.instruction_pointer < len(self.quadruples):
                quad = self.quadruples[self.instruction_pointer]
                self.execute_quad(quad)
                self.instruction_pointer += 1
        except Exception as e:
            print(f"Runtime error: {e}")

    def map_temporaries(self):
        for quad in self.quadruples:
            for elem in quad:
                if isinstance(elem, str) and elem.startswith('t'):
                    if elem not in self.temp_to_memory:
                        memory_address = self.get_next_temp_address()
                        self.temp_to_memory[elem] = memory_address
                        self.temp_vars[memory_address] = None  # Initialize with a default value



    def get_next_temp_address(self):
        address = self.temp_base_address + self.temp_counter
        self.temp_counter += 1
        return address
    

    def execute_quad(self, quad):
        op, arg1, arg2, result = quad
        if op in ('*', '/', '+', '-'):
            # Perform the operation and store the result in the temp_vars dictionary
            if op == '*':
                operation_result = self.get_value(arg1) * self.get_value(arg2)
            elif op == '/':
                divisor = self.get_value(arg2)
                if divisor == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                operation_result = self.get_value(arg1) / divisor
            elif op == '+':
                operation_result = self.get_value(arg1) + self.get_value(arg2)
            elif op == '-':
                operation_result = self.get_value(arg1) - self.get_value(arg2)
            
            # Map the result to a memory address if it's a temporary variable
            if isinstance(result, str) and result.startswith('t'):
                result_address = self.temp_to_memory.get(result)
                if result_address is None:
                    raise ValueError(f"Result variable {result} does not have a mapped memory address.")
                self.temp_vars[result_address] = operation_result
            else:
                raise ValueError(f"Invalid result operand: {result}")

            # ... handle other operations like PRINT, GOTO, etc.

        

    def get_value(self, operand):
        # If the operand is an integer or float, return it as is.
        if isinstance(operand, (int, float)):
            return operand

        # If the operand is a string that represents an integer, return the integer value.
        elif isinstance(operand, str) and operand.isdigit():
            return int(operand)

        # If the operand is a string that represents a float, return the float value.
        elif isinstance(operand, str) and self.is_float(operand):
            return float(operand)

        # If the operand is a temporary variable, retrieve its value from the temp_vars dictionary.
        elif isinstance(operand, str) and operand.startswith('t'):
            memory_address = self.temp_to_memory.get(operand)
            if memory_address is not None:
                return self.temp_vars.get(memory_address)
            else:
                raise ValueError(f"Temporary variable {operand} does not have a mapped memory address.")

        # If the operand is a global variable, retrieve its value from the global_vars dictionary.
        elif operand in self.global_vars:
            return self.global_vars[operand]['value']

        # If none of the above, the operand is invalid.
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
