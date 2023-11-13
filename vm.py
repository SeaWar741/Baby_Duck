from semanticTable import Directions
class VirtualMachine:
    def __init__(self, quadruples, varTables, functions):
        self.quadruples = quadruples
        self.memory_quadruples = [] #list of quadruples with memory directions TRANSLATED
        self.varTables = varTables
        self.global_vars = varTables['Global'].df
        self.functions = functions
        self.operand_stack = []
        self.directions = Directions()
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
        self.instruction_pointer = 0
        self.call_stack = []
        #temporals ranges
        self.temporal_addresses = (8192, 9215)

        self.temporals_values = {} #dictionary of temporals values key = memory address, value = value

    def is_variable(self, operand):
        # Check in global variables
        if operand in self.global_vars['id-name'].values:
            return True

        # Check in local variable tables
        for scope, var_table in self.varTables.items():
            if operand in var_table.df['id-name'].values:
                return True

        # Operand not found in any variable table
        return False

    def is_temporal(self, operand):
        if operand == None:
            return False
        else:
            return operand.startswith('_t')
    
    def translate_quadruples(self):
        for quad in self.quadruples:
            operator, operand1, operand2, result = quad  # Assuming this is your quadruple structure
            
            # Translate operands and result
            operand1 = self.translate_operand(operand1)
            operand2 = self.translate_operand(operand2)
            result = self.translate_operand(result)

            translated_quad = (operator, operand1, operand2, result)
            self.memory_quadruples.append(translated_quad)

    def translate_operand(self, operand):
        if self.is_variable(operand):
            # Look up in local, then global scope
            return self.lookup_memory_address(operand)
        elif self.is_temporal(operand):
            # Assign and return a unique memory address for the temporal
            return self.assign_temporal_address(operand)
        else:
            # If it's a constant or something that doesn't need translation
            return operand

    def lookup_memory_address(self, variable_name):
        # Implement the logic to find the memory address of a variable
        # Check in global variables
        if variable_name in self.global_vars['id-name'].values:
            return self.global_vars.loc[self.global_vars['id-name'] == variable_name]['direction'].values[0]
        #check in other variable tables
        for scope, var_table in self.varTables.items():
            if variable_name in var_table['id-name'].values:
                return var_table.loc[var_table['id-name'] == variable_name]['direction'].values[0]

    def assign_temporal_address(self, temporal):
        # Check if the temporal variable already has an address
        if temporal in self.temporals_values:
            return self.temporals_values[temporal]

        # Assign a new address within the specified range
        if self.temporal_addresses[0] <= self.temporal_addresses[1]:
            address = self.temporal_addresses[0]
            self.temporal_addresses = (self.temporal_addresses[0] + 1, self.temporal_addresses[1])
            self.temporals_values[temporal] = address
            return address
        else:
            # Handle the case where the address range is exhausted
            raise Exception("Out of temporal memory addresses")


    def translate_quadruples(self):
        for quad in self.quadruples:
            operator, operand1, operand2, result,scope = quad  # Assuming this is your quadruple structure
            
            # Translate operands and result
            operand1 = self.translate_operand(operand1)
            operand2 = self.translate_operand(operand2)
            result = self.translate_operand(result)

            translated_quad = (operator, operand1, operand2, result)
            self.memory_quadruples.append(translated_quad)




    def run(self):
        # Translate quadruples
        self.translate_quadruples()

        #print the quadruples
        print("Quadruples")
        for quad in self.memory_quadruples:
            print(quad)