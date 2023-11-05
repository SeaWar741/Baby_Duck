import pandas as pd

#directions reserved for ints from 1024 to 2048
#directions reserved for floats from 2048 to 3072
#directions reserved for strings from 3072 to 4096
#directions reserved for bools from 4096 to 5120
#directions reserved for functions from 5120 to 6144

class Directions:
    def __init__(self):
        #ranges as duples
        self.ints = (1024, 2048)
        self.floats = (2048, 3072)
        self.strings = (3072, 4096)
        self.bools = (4096, 5120)
        self.functions = (5120, 6144)
    
    def in_range(self, type, direction):
        #checks if the memory direction is in the range of the type, if not rise valueError exception out of memory
        if type == "int":
            if direction < self.ints[0] or direction > self.ints[1]:
                raise ValueError(f"Error: Out of memory")
        elif type == "float":
            if direction < self.floats[0] or direction > self.floats[1]:
                raise ValueError(f"Error: Out of memory")
        elif type == "string":
            if direction < self.strings[0] or direction > self.strings[1]:
                raise ValueError(f"Error: Out of memory")
        elif type == "bool":
            if direction < self.bools[0] or direction > self.bools[1]:
                raise ValueError(f"Error: Out of memory")
        elif type == "function":
            if direction < self.functions[0] or direction > self.functions[1]:
                raise ValueError(f"Error: Out of memory")

    def get_type(self,direction):
        #returns the type of data
        if direction >= self.ints[0] and direction <= self.ints[1]:
            return "int"
        elif direction >= self.floats[0] and direction <= self.floats[1]:
            return "float"
        elif direction >= self.strings[0] and direction <= self.strings[1]:
            return "string"
        elif direction >= self.bools[0] and direction <= self.bools[1]:
            return "bool"
        elif direction >= self.functions[0] and direction <= self.functions[1]:
            return "function"

    def get_type_range(self,type):
        #returns the range of the type
        if type == "int":
            return self.ints
        elif type == "float":
            return self.floats
        elif type == "string":
            return self.strings
        elif type == "bool":
            return self.bools
        elif type == "function":
            return self.functions
        
    

class DirFunc:
    def __init__(self):
        self.df = pd.DataFrame(columns=["id-name", "scope","var-table"])
        
    def add_func(self, id_name, func_type, scope="Global"):
        if id_name in self.df["id-name"].values:
            raise ValueError(f"Error: Multiple declaration of {id_name}")
        self.df.loc[len(self.df)] = [id_name, func_type, scope]

    def delete(self):
        self.df = pd.DataFrame(columns=["id-name", "scope","var-table"])

class VarTable:
    def __init__(self):
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope", "direction"])
        self.directions = Directions()  # Create an instance of Directions within VarTable

    def add_var(self, id_name, var_type, value=None, scope="Global", direction=None):
        if id_name in self.df["id-name"].values:
            raise ValueError(f"Error: Multiple declaration of {id_name}")
        
        if direction is None:
            # Get the range of the type
            type_range = self.directions.get_type_range(var_type)
            # Get the direction of the type
            direction = type_range[0]
            # Set the direction of the type to the next available direction, check the variable table also
            while direction in self.df["direction"].values:
                direction += 1
            # Check if the direction is in the range of the type
            self.directions.in_range(var_type, direction)
        # Add the variable to the table
        self.df.loc[len(self.df)] = [id_name, var_type, value, scope, direction]


    def delete(self):
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope","direction"])
