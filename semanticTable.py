import pandas as pd

#GLOBAL VARIABLES
#directions reserved for ints from 1024 to 2048
#directions reserved for floats from 2048 to 3072
#directions reserved for strings from 3072 to 4096
#directions reserved for bools from 4096 to 5120

#TEMPORALS
#directions reserved for functions from 5120 to 6144

#LOCAL VARIABLES
#directions reserved for ints from 6144 to 7168
#directions reserved for floats from 7168 to 8192

class Directions:
    def __init__(self):
        # ranges as tuples
        self.global_ints = (1024, 2047)
        self.global_floats = (2048, 3071)
        self.global_strings = (3072, 4095)
        self.global_bools = (4096, 5119)
        self.functions = (5120, 6143)
        self.local_ints = (6144, 7167)
        self.local_floats = (7168, 8191)
        # Add more ranges for local strings and bools if needed
    
    def in_range(self, var_type, direction, scope):
        # checks if the memory direction is in the range of the type, if not raise ValueError exception out of memory
        if scope == "Global":
            ranges = {
                "int": self.global_ints,
                "float": self.global_floats,
                "string": self.global_strings,
                "bool": self.global_bools,
            }
        else:  # Local scope
            ranges = {
                "int": self.local_ints,
                "float": self.local_floats,
                # Add more checks for local strings and bools if needed
            }
        if direction < ranges[var_type][0] or direction > ranges[var_type][1]:
            raise ValueError(f"Error: Out of memory for {var_type} in {scope} scope")

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

    def get_type_range(self, var_type, scope):
        # returns the range of the type depending on the scope
        if scope == "Global":
            ranges = {
                "int": self.global_ints,
                "float": self.global_floats,
                "string": self.global_strings,
                "bool": self.global_bools,
                "function": self.functions,
            }
        else:  # Local scope
            ranges = {
                "int": self.local_ints,
                "float": self.local_floats,
                # Add more ranges for local strings and bools if needed
            }
        return ranges[var_type]
    
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
        if id_name in self.df[self.df["scope"] == scope]["id-name"].values:
            raise ValueError(f"Error: Multiple declaration of {id_name} in {scope} scope")

        if direction is None:
            # Get the range of the type depending on the scope
            type_range = self.directions.get_type_range(var_type, scope)
            # Set the direction of the type to the next available direction within the range
            direction = type_range[0]
            while direction in self.df[self.df["scope"] == scope]["direction"].values:
                direction += 1
                if direction > type_range[1]:
                    raise ValueError(f"Error: Out of memory for {var_type} in {scope} scope")

        else:
            # Check if the direction is in the range of the type depending on the scope
            self.directions.in_range(var_type, direction, scope)

        # Add the variable to the table
        self.df.loc[len(self.df)] = [id_name, var_type, value, scope, direction]

    def delete(self):
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope", "direction"])


