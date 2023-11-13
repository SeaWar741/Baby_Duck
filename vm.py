from semanticTable import Directions

import re


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

        self.placeholders_range_ranges = [self.placeholders]

        self.int_ranges = [self.temporal_ints_global,self.temporal_ints_local,self.constant_ints]
        self.float_ranges = [self.temporal_floats_global,self.temporal_floats_local,self.constant_floats]
        self.bool_ranges = [self.temporal_bools_global,self.temporal_bools_local,self.constant_bools]
        self.string_ranges = [self.constant_strings]
        self.placeholder_ranges = [self.placeholders]


        self.temporals_values = {} #dictionary of temporals values key = memory address, value = (value,name)
        self.constants_values = {} #dictionary of constants values key = memory address, value = (value,name)
        self.placeholders_values = {}

        self.temporals_data = {} #dictionary of temporals data key = memory address,value
        self.constants_data = {} #dictionary of constants data key = memory address,value
        self.placeholders_data = {} #dictionary of placeholders data key = memory address,value


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

    def detranslate_variable(self, direction):
        # Implement the logic to find the variable name of a memory address
        # Check in global variables
        if direction in self.global_vars['direction'].values:
            return self.global_vars.loc[self.global_vars['direction'] == direction]['id-name'].values[0]
        else:
            #check in other variable tables
            for scope, var_table in self.varTables.items():
                if direction in var_table.df['direction'].values:
                    return var_table.df.loc[var_table.df['direction'] == direction]['id-name'].values[0]
    
    def print_temporals(self):
        print("\nTemporals:")
        for key, value in self.temporals_values.items():
            print(key, value)

    def assignAddressTemporals(self, temporal, temporal_type, scope):
        # Check if the temporal has already been assigned a memory address
        if temporal in self.temporals_values:
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
        #add the temporal to the temporals_data dictionary
        self.temporals_data[memory_address] = None

        # Return the memory address
        return memory_address
               

    def getConstantType(self,constant):
        #checks if its numeric using regex
        if re.match(r'^-?\d+(?:\.\d+)?$', constant):
            #checks if its an int
            if constant.isnumeric():
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
        else:
            print("ERROR: Invalid constant type "+constant)

    def printstacks(self):
        print("\nOperand Stack:")
        print(self.operand_stack)
        print("\nTemporals Values:")
        print(self.temporals_values)
        print("\nTemporals Data:")
        print(self.temporals_data)
        print("\nConstants Values:")
        print(self.constants_values)
        print("\nConstants Data:")
        print(self.constants_data)
        print("\nPlaceholders Values:")
        print(self.placeholders_values)
        print("\nPlaceholders Data:")
        print(self.placeholders_data)

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

    def translate_constant(self,element):
        dtype = self.getConstantType(element)

        address = self.assignAddressConstants(element)

        self.setValue(address,element)

        return address

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

                                address = self.translate_constant(element)

                                translated_quad.append(address)
                                self.operand_stack.append(address)

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

    def not_memory_address(self,element):
        #checks if element is a memory address
        if element in self.temporals_values.keys():
            return False
        else:
            return True

    def check_in_range(self,element,start,end):
        #checks if element is in range
        if element >= start and element <= end:
            return True
        else:
            return False

    def setValue(self, memory_address, value):

        #check the ranges of the memory address to know what type of value it is and cast it
        for range in self.int_ranges:
            if self.check_in_range(memory_address,range[0],range[1]):
                value = int(value)
                break
        for range in self.float_ranges:
            if self.check_in_range(memory_address,range[0],range[1]):
                value = float(value)
                break
        for range in self.bool_ranges:
            if self.check_in_range(memory_address,range[0],range[1]):
                if value == "true":
                    value = True
                elif value == "false":
                    value = False
                break
        for range in self.string_ranges:
            if self.check_in_range(memory_address,range[0],range[1]):
                value = str(value)
                break
        for range in self.placeholder_ranges:
            if self.check_in_range(memory_address,range[0],range[1]):
                value = str(value)
                break


    
        #if its on the temporals_values then set the value in temporals_data
        if memory_address in self.temporals_values.keys():
            self.temporals_data[memory_address] = value

        #if its on the constants_values then set the value in constants_data
        elif memory_address in self.constants_values.keys():
            self.constants_data[memory_address] = value
        
        #if its on the placeholders_values then set the value in placeholders_data
        elif memory_address in self.placeholders_values.keys():
            self.placeholders_data[memory_address] = value

        #set the value to the variable in the varTable
        #check if the memory address is in the global varTable
        elif memory_address in self.global_vars['direction'].values:
            self.global_vars.loc[self.global_vars['direction'] == memory_address, 'value'] = value
        else:
            #check in other variable tables
            for scope, var_table in self.varTables.items():
                if memory_address in var_table.df['direction'].values:
                    var_table.df.loc[var_table.df['direction'] == memory_address, 'value'] = value

        

    def getValue(self, memory_address):
        #check if the memory address is in the temporals_values
        if memory_address in self.temporals_values.keys():
            return self.temporals_data[memory_address]
        #check if the memory address is in the constants
        elif memory_address in self.constants_values.keys():
            return self.constants_data[memory_address]
        #check if the memory address is in the placeholders
        elif memory_address in self.placeholders_values.keys():
            return self.placeholders_data[memory_address]

        #get the value of the variable on the memory address. check the varTables,temporals_values,constants
        #check if the memory address is in the global varTable
        elif memory_address in self.global_vars['direction'].values:
            return self.global_vars.loc[self.global_vars['direction'] == memory_address, 'value'].values[0]
        else:
            #check in other variable tables
            for scope, var_table in self.varTables.items():
                if memory_address in var_table.df['direction'].values:
                    return var_table.df.loc[var_table.df['direction'] == memory_address, 'value'].values[0]
            #check if the memory address is in the temporals_values
            if memory_address in self.temporals_values.keys():
                return self.temporals_values[memory_address]
            else:
                #check if the memory address is in the constants
                for key, value in self.temporals_values.items():
                    if value == memory_address:
                        return key
        


    def execute_quadruple(self, quad):
        op, left_operand, right_operand, result = quad

        #print("Attempting to execute quadruple: ", quad)
        #self.printstacks()

        left_value = self.getValue(left_operand)
        right_value = self.getValue(right_operand)

        # Assignment operation
        if op == "=":
            value = self.getValue(left_operand)
            self.setValue(result, value)

        # Arithmetic operations
        elif op in ['+', '-', '*', '/']:

            if op == '+':
                result_value = left_value + right_value
            elif op == '-':
                result_value = left_value - right_value
            elif op == '*':
                result_value = left_value * right_value
            elif op == '/':
                result_value = left_value / right_value

            self.setValue(result, result_value)

        # Relational operations
        elif op in ['>', '<', '>=', '<=', '!=']:

            if op == '>':
                result_value = left_value > right_value
            elif op == '<':
                result_value = left_value < right_value
            elif op == '>=':
                result_value = left_value >= right_value
            elif op == '<=':
                result_value = left_value <= right_value
            elif op == '!=':
                result_value = left_value != right_value

            self.setValue(result, result_value)
        
        # Print operation
        elif op == 'PRINT':
            print(left_value)






    def execute_quadruples(self):
        #execute quadruples with instruction pointer
        while self.instruction_pointer < len(self.memory_quadruples):
            quad = self.memory_quadruples[self.instruction_pointer]
            self.execute_quadruple(quad)
            self.instruction_pointer += 1

    def run(self):
        # Translate quadruples
        self.translate_quadruples()
        self.printTranslatedQuadruples()
        # Execute quadruples
        self.execute_quadruples()


        #print varTables
        for scope, var_table in self.varTables.items():
            print(f"\n{scope} varTable:")
            print(var_table.df)