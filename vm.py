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

        self.reserved_words = ["GOTO","CALL","END","PARAM","GOTO_F","GOTO_T","ERA","GOSUB","RETURN","ENDPROC"]

        #temporals ranges
        self.temporal_ints_global = (8192, 9215)
        self.temporal_floats_global = (9216, 10240)
        self.temporal_bools_global = (10240, 11263)

        self.temporal_ints_local = (11264, 12287)
        self.temporal_floats_local = (12288, 13312)
        self.temporal_bools_local = (13312, 14335)

        #constants ranges
        self.constant_ints = (14336, 15359)
        self.constant_floats = (15360, 16383)
        self.constant_bools = (16384, 17407)
        self.constant_strings = (17408, 18431)

        #placeholder/label ranges
        self.placeholders = (18432, 19455)


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

    def getConstantType(self,constant):
        #checks if its numeric
        if constant.isnumeric():
            #checks if its an integer
            if constant.isdigit():
                return "int"
            #checks if its a float
            else:
                return "float"
        #checks if its a string
        elif constant.startswith('"') and constant.endswith('"'):
            return "string"
        #checks if its a boolean
        elif constant == "true" or constant == "false":
            return "bool"
        elif constant.startswith('P') or constant.startswith('L'):
            return "placeholder"


    #TENTATIVE
    def assignAddressConstants(self, constant):
        # Determine the range to use based on the type and scope
        constant_type = self.getConstantType(constant)
        if constant_type == 'int':
            memory_address = self.constant_ints[0]
            self.constant_ints = (self.constant_ints[0] + 1, self.constant_ints[1])
        elif constant_type == 'float':
            memory_address = self.constant_floats[0]
            self.constant_floats = (self.constant_floats[0] + 1, self.constant_floats[1])
        elif constant_type == 'bool':
            memory_address = self.constant_bools[0]
            self.constant_bools = (self.constant_bools[0] + 1, self.constant_bools[1])
        elif constant_type == 'string':
            memory_address = self.constant_strings[0]
            self.constant_strings = (self.constant_strings[0] + 1, self.constant_strings[1])
        elif constant_type == 'placeholder':
            memory_address = self.placeholders[0]
            self.placeholders = (self.placeholders[0] + 1, self.placeholders[1])
        else:
            raise ValueError("Invalid constant type")

        # Add the constant to the temporals_values dictionary
        self.temporals_values[memory_address] = constant

        # Return the memory address
        return memory_address



    def translate_quadruples(self):
        for quad in self.quadruples:
            translated_quad = []
            count = 0


            if len(quad) > 4:

                #if first element in quad is a CALL then dont translate
                if quad[0] not in self.reserved_words:
                    for element in quad:
                        if count < 4:
                            if element == None:
                                translated_quad.append(None)
                            elif element == "PRINT":
                                translated_quad.append("PRINT")
                            elif self.is_operator(element):
                                # Operators might not need translation
                                translated_quad.append(element)
                            elif self.is_label_or_function_name(element):
                                # Labels and function names might not need translation
                                translated_quad.append(element)
                                self.operand_stack.append(element)
                            elif self.is_variable(element):
                                translated_var = self.translate_variable(element)
                                translated_quad.append(translated_var)
                                self.operand_stack.append(translated_var)
                            elif element.startswith('_t'):
                                #check if the element is already in temporals_values as value. not as key
                                if element in self.temporals_values.values():
                                    #if it is, then just append the memory address
                                    translated_quad.append(element)
                                    self.operand_stack.append(element)
                                else:
                                    #if it is not, then assign a memory address to the temporal
                                    #and append the memory address
                                    address = self.assignAddressTemporals(element,self.var_types[element],quad[4])
                                    self.temporals_values[address] = None
                                    translated_quad.append(address)
                                    self.operand_stack.append(address)
                            else:
                                # Constants might not need translation
                                #print("Constant: ",element)

                                #address = self.assignAddressConstants(element)

                                translated_quad.append(element)
                                self.operand_stack.append(element)

                        count += 1
                else:
                    #if the first element is a CALL then dont translate
                    translated_quad = quad[0:4]
            else:
                #instructions only no need to translate
                self.operand_stack.append(quad[0])
                translated_quad = quad
               
            self.memory_quadruples.append(translated_quad)


            print("------------------------------------------------------------------------")
            print("QuadT: ",quad)
            print("QuadT: ",translated_quad)
    
    def printTranslatedQuadruples(self):
        print("\nTranslated Quadruples:")
        for quad in self.memory_quadruples:
            print(quad)

        print("Operand Stack")
        print(self.operand_stack)


    def get_value(self, memory_address):
        
        

        # Check if the memory address is in the temporals_values dictionary
        if memory_address in self.temporals_values.keys():
            # Return the value of the temporal
            return self.temporals_values[memory_address]
        else:
            # check for value in varTables
            for scope, var_table in self.varTables.items():
                if memory_address in var_table.df['direction'].values:
                    return var_table.df.loc[var_table.df['direction'] == memory_address]['value'].values[0]
            #if not found in varTables then return error
            raise ValueError(f"Error: Memory address {memory_address} not found")
        
    def perform_arithmetic(self, operation, operand1, operand2):

        if operation == '+':
            return int(operand1) + int(operand2)
        elif operation == '-':
            return int(operand1) - int(operand2)
        elif operation == '*':
            return int(operand1) * int(operand2)
        elif operation == '/':
            return int(operand1) / int(operand2)
        elif operation == '>':
            return int(operand1) > int(operand2)
        elif operation == '<':
            return int(operand1) < int(operand2)
        elif operation == '>=':
            return int(operand1) >= int(operand2)
        elif operation == '<=':
            return int(operand1) <= int(operand2)
        elif operation == "!=":
            return int(operand1) != int(operand2)
        else:
            raise ValueError(f"Error: Invalid operation {operation}")
    
    def set_value(self, memory_address, value):
        # Check if the memory address is in the temporals_values dictionary
        if memory_address in self.temporals_values.keys():
            # Set the value of the temporal
            self.temporals_values[memory_address] = value
        else:
            # check for value in varTables
            for scope, var_table in self.varTables.items():
                if memory_address in var_table.df['direction'].values:
                    var_table.df.loc[var_table.df['direction'] == memory_address, 'value'] = value
                    return
            #if not found in varTables then return error
            raise ValueError(f"Error: Memory address {memory_address} not found")

    def execute_quadruples(self):
        while self.instruction_pointer < len(self.memory_quadruples):
            quad = self.memory_quadruples[self.instruction_pointer]
            operation = quad[0]


            """ 
            if operation == 'GOTO':
                #TODO: check if the label exists
                pass

            elif operation == '=':
                # Assignment operation
                value = self.get_value(quad[1])
                self.set_value(quad[3], value)

            elif operation in ['+', '-', '*', '/']:
                # Arithmetic operations
                operand1 = self.get_value(quad[1])
                operand2 = self.get_value(quad[2])
                result = self.perform_arithmetic(operation, operand1, operand2)
                self.set_value(quad[3], result)

            elif operation == '=':
                # Assignment operation
                value = self.get_value(quad[1])
                self.set_value(quad[3], value)

            elif operation == 'PRINT':
                # Print operation
                #if the value is a memory address then get the value from the memory address else just print the value
                if quad[3] in self.temporals_values.keys():
                    value = self.temporals_values[quad[3]]
                else:
                    value = quad[3]
                print(value)

            elif operation == 'END':
                break """

            self.instruction_pointer += 1

                



    def run(self):
        # Translate quadruples
        self.translate_quadruples()
        self.printTranslatedQuadruples()
        # Execute quadruples
        self.execute_quadruples()
