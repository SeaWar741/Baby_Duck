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
        
        self.temporal_ints = (8192, 9215)
        self.temporal_floats = (9216, 10240)
        self.temporal_bools = (10240, 11263)




        self.temporals_values = {} #dictionary of temporals values key = memory address, value = value

    def printVarTables(self):
        for scope, var_table in self.varTables.items():
            print(f"\nScope: {scope}")
            print(var_table.df)

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
            try:
                return operand.startswith('_t')
            except:
                return False

    def translate_quadruples(self):
        for quad in self.quadruples:
            operator, operand1, operand2, result = quad  # Assuming this is your quadruple structure
            
            #HERE HOW CAN I KNOW THE TYPE OF THE OPERANDS AND THE RESULT?

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
            # Assign and return a unique memory address for the temporal based on its type
            return self.assign_temporal_address(operand,operand_type)
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
            if variable_name in var_table.df['id-name'].values:
                return var_table.df.loc[var_table.df['id-name'] == variable_name]['direction'].values[0]

    def lookup_variable_from_address(self, address):
        # Implement the logic to find the variable name from a memory address
        # Check in global variables
        if address in self.global_vars['direction'].values:
            return self.global_vars.loc[self.global_vars['direction'] == address]['id-name'].values[0]
        #check in other variable tables
        for scope, var_table in self.varTables.items():
            if address in var_table.df['direction'].values:
                return var_table.df.loc[var_table.df['direction'] == address]['id-name'].values[0]

    def lookup_type_from_address(self, address):
        # Implement the logic to find the type from a memory address
        # Check in global variables
        if address in self.global_vars['direction'].values:
            return self.global_vars.loc[self.global_vars['direction'] == address]['type'].values[0]
        #check in other variable tables
        for scope, var_table in self.varTables.items():
            if address in var_table.df['direction'].values:
                return var_table.df.loc[var_table.df['direction'] == address]['type'].values[0]
            
    def lookup_type_from_variable(self, variable_name):
        # Implement the logic to find the type from a variable name
        # Check in global variables
        if variable_name in self.global_vars['id-name'].values:
            return self.global_vars.loc[self.global_vars['id-name'] == variable_name]['type'].values[0]
        #check in other variable tables
        for scope, var_table in self.varTables.items():
            if variable_name in var_table.df['id-name'].values:
                return var_table.df.loc[var_table.df['id-name'] == variable_name]['type'].values[0]

    def assign_temporal_address(self, temporal, temporal_type):
        # Check if the temporal variable already has an address
        if temporal in self.temporals_values.keys():
            return self.temporals_values[temporal]
        else:
            # Get the range of the type depending on the scope
            type_range = self.get_type_range(temporal_type, scope="Temporal")
            # Set the direction of the type to the next available direction within the range
            direction = type_range[0]
            while direction in self.temporals_values.keys():
                direction += 1
                if direction > type_range[1]:
                    raise ValueError(f"Error: Out of memory for {temporal_type} in Temporal scope")

            # Add the variable to the table
            self.temporals_values[temporal] = direction
            return direction


    def translate_quadruples(self):
        for quad in self.quadruples:
            operator, operand1, operand2, result,scope = quad  # Assuming this is your quadruple structure
            print("------------------------------------------------------------------------")
            print("QuadT: ",quad)
            

            # Translate operands and result
            operand1 = self.translate_operand(operand1)
            operand2 = self.translate_operand(operand2)
            result = self.translate_operand(result)

            translated_quad = (operator, operand1, operand2, result)
            self.memory_quadruples.append(translated_quad)

            #print("QuadT: ",translated_quad)
            self.printVarTables()

    def run(self):
        # Translate quadruples
        self.translate_quadruples()
