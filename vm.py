from semanticTable import Directions
class VirtualMachine:
    def __init__(self, quadruples, varTables, functions,var_types,operand_stack):
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

        self.var_types = var_types
        self.operand_stack = operand_stack

        #temporals ranges
        self.temporal_ints_global = (8192, 9215)
        self.temporal_floats_global = (9216, 10240)
        self.temporal_bools_global = (10240, 11263)

        self.temporal_ints_local = (11264, 12287)
        self.temporal_floats_local = (12288, 13312)
        self.temporal_bools_local = (13312, 14335)


        self.temporals_values = {} #dictionary of temporals values key = memory address, value = value


    def is_operator(self, element):
        return element in ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', '&&', '||', '=']
    
    def is_label_or_function_name(self, element):
        instructions = ["LABEL", "GOTO","CALL","PARAM","GOTO_F"]

        if element in self.functions:
            return True
        elif element in instructions:
            return True
        else:
            return False

    def is_variable(self, element):
        #check if element is a variable in any varTable
        for scope, var_table in self.varTables.items():
            if element in var_table.df['id-name'].values:
                return True
            
    def translate_variable(self, element):
        # Implement the logic to find the memory address of a variable
        # Check in global variables
        if element in self.global_vars['id-name'].values:
            return self.global_vars.loc[self.global_vars['id-name'] == element]['direction'].values[0]
        else:
            #check in other variable tables
            for scope, var_table in self.varTables.items():
                if element in var_table.df['id-name'].values:
                    return var_table.df.loc[var_table.df['id-name'] == element]['direction'].values[0]


    def assignAddressTemporals(self, temporal, temporal_type, scope):
        # Check if the temporal has already been assigned a memory address
        if temporal in self.temporals_values.values():
            # Return the existing memory address
            return self.temporals_values[temporal]

        # Determine the range to use based on the type and scope
        if temporal_type == 'int':
            if scope == 'Global':
                memory_address = self.temporal_ints_global[0]
                self.temporal_ints_global = (self.temporal_ints_global[0] + 1, self.temporal_ints_global[1])
            else:
                memory_address = self.temporal_ints_local[0]
                self.temporal_ints_local = (self.temporal_ints_local[0] + 1, self.temporal_ints_local[1])
        elif temporal_type == 'float':
            if scope == 'Global':
                memory_address = self.temporal_floats_global[0]
                self.temporal_floats_global = (self.temporal_floats_global[0] + 1, self.temporal_floats_global[1])
            else:
                memory_address = self.temporal_floats_local[0]
                self.temporal_floats_local = (self.temporal_floats_local[0] + 1, self.temporal_floats_local[1])
        elif temporal_type == 'bool':
            if scope == 'Global':
                memory_address = self.temporal_bools_global[0]
                self.temporal_bools_global = (self.temporal_bools_global[0] + 1, self.temporal_bools_global[1])
            else:
                memory_address = self.temporal_bools_local[0]
                self.temporal_bools_local = (self.temporal_bools_local[0] + 1, self.temporal_bools_local[1])
        else:
            raise ValueError("Invalid temporal type")

        # Add the temporal to the temporals_values dictionary
        self.temporals_values[temporal] = memory_address

        # Return the memory address
        return memory_address

    def translate_quadruples(self):
        for quad in self.quadruples:
            translated_quad = []
            count = 0

            for element in quad:
                if count < 4:
                    if element == None:
                        translated_quad.append(None)
                    elif self.is_operator(element):
                        # Operators might not need translation
                        translated_quad.append(element)
                    elif self.is_label_or_function_name(element):
                        # Labels and function names might not need translation
                        translated_quad.append(element)
                    elif self.is_variable(element):
                        translated_quad.append(self.translate_variable(element))
                    elif element.startswith('_t'):
                        #check if the element is already in temporals_values as value. not as key
                        if element in self.temporals_values.values():
                            #if it is, then just append the memory address
                            translated_quad.append(element)
                        else:
                            #if it is not, then assign a memory address to the temporal
                            #and append the memory address
                            address = self.assignAddressTemporals(element,self.var_types[element],quad[4])
                            self.temporals_values[address] = None
                            translated_quad.append(address)
                    else:
                        # Constants might not need translation
                        translated_quad.append(element)

                count += 1
               
            self.memory_quadruples.append(translated_quad)


            print("------------------------------------------------------------------------")
            print("QuadT: ",quad)
            print("QuadT: ",translated_quad)
            #self.printVarTables()

    def run(self):
        # Translate quadruples
        self.translate_quadruples()
