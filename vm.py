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

        self.reserved_words = ["GOTO","CALL","END","PARAM","GOTO_F","GOTO_T","ERA","GOSUB","RETURN","ENDPROC","PRINT"]

        #temporals ranges
        self.temporal_ints_global = (8192, 9215)
        self.temporal_floats_global = (9216, 10240)
        self.temporal_bools_global = (10241, 11263)


        self.temporal_ints_local = (11264, 12287)
        self.temporal_floats_local = (12288, 13312)
        self.temporal_bools_local = (13313, 14335)


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

        self.placeholders_positions = {} #dictionary of placeholders positions key = placeholder name, value = position in quadruples

        self.end_cycle_positions = [] #list of positions of the end of cycles youve entered

    def printvariableTables(self):
        #print varTables
        for scope, var_table in self.varTables.items():
            print(f"\n{scope} varTable:")
            print(var_table.df)

    def is_operator(self, element):
        return element in ['+', '-', '*', '/', '>', '<', '>=', '<=', '==', '!=', '&&', '||', '=']
    
    def is_label_or_function_name(self, element):
        instructions = ["LABEL", "GOTO","CALL","GOTO_F","GOTO_T","ERA","GOSUB","RETURN","ENDPROC","PRINT"]

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
        count2 = 0
        for quad in self.quadruples:
            translated_quad = []
            count = 0
            

            if len(quad) > 4:

                #if first element in quad is a CALL then dont translate
                if quad[0] == "CALL":
                    translated_quad = quad
                    raise NotImplementedError("CALL operation not implemented, methods not implemented")
                else:

                    for element in quad:
                        if count < 4:
                            if element == None:
                                translated_quad.append(None)
                            elif element in self.reserved_words:
                                translated_quad.append(element)
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
                print("QUAD INSTRUCTION")
                for element in quad:
                    if element == None:
                        translated_quad.append(None)
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
                            address = self.assignAddressTemporals(element,self.var_types[element],"Global")
                            self.temporals_values[address] = None
                            translated_quad.append(address)
                            self.operand_stack.append(address)

                    
            self.memory_quadruples.append(translated_quad)

            #if first quad print line
            
            if count2 > 0:
                print("---------------------------------------------------------------------")

            print("QuadT: ",quad)
            print("QuadT: ",translated_quad)
            count2 += 1

    
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
                #check if the memory address is in the placeholders
                for key, value in self.placeholders_values.items():
                    if value == memory_address:
                        return key

    

    def findQuadruple_index(self,quad):
        #find the index of the quadruple in the memory_quadruples based on the placeholders_values. 
        #meaning i have as target P3, i should find the index where P4 or L4 is in the quadruple. The L and P are the same
        #so i can go and execute the quadruple after the placeholder

        #get the placeholder from the address
        placeholder = self.temporals_data[quad[1]]
        
        #print(placeholder)
                
        #if nothing is found it means that the Lable, Placeholder or GOTO is the last target so execute the next quadruple
        #print("MOVING ON")
        return self.instruction_pointer + 1
    

    def jumpingDirections(self,target):
        #iterate over the quads and find the quadruple with the next label or placeholder
        #if the quadruple is a label or placeholder then return the index of the quadruple
        for quad in self.memory_quadruples:
            if quad[-1][1:] == target[1:]:
                return self.memory_quadruples.index(quad)
        #if nothing is found it means that the Lable, Placeholder or GOTO is the last target so execute the next quadruple
        self.instruction_pointer + 1


    def mapPlaceholders(self):
        #iterate over the quadruples and find the placeholders, then map each placeholder memory address to the quadruple index and add to the
        #placeholders values dictionary
        for quad in self.quadruples:
            #if it doesnt exist in the placeholders_values then add it
            if quad[1] not in self.placeholders_positions.keys():
                if quad[0] == "LABEL":
                    self.placeholders_positions[quad[1]] = self.quadruples.index(quad)
                elif quad[0] == "GOTO":
                    self.placeholders_positions[quad[1]] = self.quadruples.index(quad)
                elif quad[0] == "GOTO_F":
                    self.placeholders_positions[quad[1]] = self.quadruples.index(quad)
                elif quad[0] == "GOTO_T":
                    self.placeholders_positions[quad[1]] = self.quadruples.index(quad)
                elif quad[0] == "CALL":
                    self.placeholders_positions[quad[1]] = self.quadruples.index(quad)
                elif quad[0] == "END":
                    self.placeholders_positions[quad[1]] = len(self.quadruples)


    def findFirstAppearance(self,element):
        #go through the placeholders_positions and find the first appearance of the element based on the value in memory
        for key, value in self.placeholders_positions.items():
            if self.getValue(value) == element:
                return key



    def execute_quadruple(self, quad):
        
        if len(quad) == 4:
            op, left_operand, right_operand, result = quad

            print("Attempting to execute quadruple: ", self.quadruples[self.instruction_pointer])
            #print quadruples values
            print("Quadruple values: ", end=" ")
            

            left_value = self.getValue(left_operand)
            right_value = self.getValue(right_operand)

            try:
                print(left_value, right_value,self.getValue(result))
            except:
                pass


            self.printstacks()
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
                    #check for division by zero
                    if right_value == 0:
                        raise ValueError("Division by zero")
                    else:

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
                #if string then strip the quotes
                if isinstance(left_value, str):
                    left_value = left_value[1:-1]
                print(left_value)

            # Control flow operations
            elif op in ['GOTO_T']:
                self.jumpingDirections(right_operand)
            elif op in ['GOTO']:
                if right_value != None and left_value != None and self.instruction_pointer !=0:
                    print("REPEAT")
                    print(left_operand,":",left_value)
                    print(self.placeholders_positions)
                    print(str(self.placeholders_positions[left_value]))
                    print(self.placeholders_data)
                    print(self.end_cycle_positions)
                    self.printvariableTables()
                    print()
                    #apppend the current position to the end_cycle_positions +1 so it can go to the next quadruple
                    self.end_cycle_positions.append(self.instruction_pointer+1)
                    self.instruction_pointer = self.placeholders_positions[left_value]
            
            elif op in ['GOTO_F']:
                #if the operand is then end of a cycle then pop the end_cycle_positions and go to the next quadruple
                if left_value == False:
                    print("ATTEMPTING END OF CYCLE")
                    self.instruction_pointer = self.end_cycle_positions.pop()
                    

            elif op == ["PARAM"]:
                raise NotImplementedError("PARAM operation not implemented, methods not implemented")

        
        elif len(quad) == 3:
            op, left_operand, result = quad

            # Control flow operations
            if op in ['GOTO', 'GOTO_F', 'GOTO_T']:
                # GOTO_F operation
                if op == "GOTO_F":
                    condition_value = self.getValue(left_operand)
                    print("Condition value: ", condition_value)
                    if not condition_value:  # If condition is false
                        self.instruction_pointer = self.findQuadruple_index(quad)  # Jump to quadruple after label
                    else:
                        self.instruction_pointer += self.findQuadruple_index(quad)  # Move to next quadruple
                    return
                

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
        self.printstacks()

        print("\n-----------------------------------------------------------------------")
        print("CODE EXECUTION")
        print("-----------------------------------------------------------------------")

        #map placeholders
        self.mapPlaceholders()

        # Execute quadruples
        self.execute_quadruples()

        print("-----------------------------------------------------------------------")
        print("CODE EXECUTION FINISHED")
        print("-----------------------------------------------------------------------")

        self.printvariableTables()