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

#RANGE FOR TEMPORALS
#directions reserved for ints from 8192 to 9216
#directions reserved for floats from 9216 to 10240

class Directions:
    """
    This class represents the memory ranges for different data types and scopes in a programming language.
    It provides methods to check if a memory direction is within the range of a certain data type and scope, 
    to get the type of data stored in a certain memory direction, and to get the range of a certain data type 
    depending on the scope.
    """
    def __init__(self):
        # ranges as tuples
        self.global_ints = (1024, 2047)
        self.global_floats = (2048, 3071)
        self.global_strings = (3072, 4095)
        self.global_bools = (4096, 5119)
        self.functions = (5120, 6143)
        self.local_ints = (6144, 7167)
        self.local_floats = (7168, 8191)
        self.local_bools = (8192, 9215)
        self.temporal_ints = (8192, 9215)
        self.temporal_floats = (9216, 10240)
        self.temporal_bools = (10240, 11263)
        # Add more ranges for local strings and bools if needed
    
    def in_range(self, var_type, direction, scope):
        """
        Checks if the memory direction is within the range of the specified data type and scope.
        If the direction is out of range, raises a ValueError exception with an error message.
        
        Parameters:
        var_type (str): The data type to check. Possible values: "int", "float", "string", "bool".
        direction (int): The memory direction to check.
        scope (str): The scope to check. Possible values: "Global", "Local".
        
        Raises:
        ValueError: If the memory direction is out of range for the specified data type and scope.
        """
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
        """
        Returns the type of data stored in the specified memory direction.
        
        Parameters:
        direction (int): The memory direction to check.
        
        Returns:
        str: The type of data stored in the specified memory direction. Possible values: "int", "float", "string", "bool", "function".
        """
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
        """
        Returns the memory range for the specified data type and scope.
        
        Parameters:
        var_type (str): The data type to check. Possible values: "int", "float", "string", "bool", "function".
        scope (str): The scope to check. Possible values: "Global", "Local".
        
        Returns:
        tuple: The memory range for the specified data type and scope.
        """
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
        self.df = pd.DataFrame(columns=["id-name", "scope","var-table","starting_quad","ending_quad"])
        
    def add_func(self, id_name, func_type, scope="Global",starting_quad=None,ending_quad=None):
        if id_name in self.df["id-name"].values:
            raise ValueError(f"Error: Multiple declaration of {id_name}")
        self.df.loc[len(self.df)] = [id_name, func_type, scope,starting_quad,ending_quad]

    def delete(self):
        self.df = pd.DataFrame(columns=["id-name", "scope","var-table","starting_quad","ending_quad"])



class VarTable:
    """
    A class used to represent a variable table.

    Attributes
    ----------
    df : pandas.DataFrame
        a dataframe containing the variables' information
    directions : Directions
        an instance of Directions class

    Methods
    -------
    add_var(id_name, var_type, value=None, scope="Global", direction=None)
        Adds a variable to the table
    delete()
        Deletes all variables from the table
    get_memory_direction(target)
        Returns the memory direction of the target variable
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the VarTable object.

        Parameters
        ----------
        None
        """
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope", "direction"])
        self.directions = Directions()  # Create an instance of Directions within VarTable

    def add_var(self, id_name, var_type, value=None, scope="Global", direction=None):
        """
        Adds a variable to the table.

        Parameters
        ----------
        id_name : str
            the name of the variable
        var_type : str
            the type of the variable
        value : any, optional
            the value of the variable, by default None
        scope : str, optional
            the scope of the variable, by default "Global"
        direction : int, optional
            the memory direction of the variable, by default None

        Raises
        ------
        ValueError
            if there is a multiple declaration of the variable in the same scope or if there is no memory available for the variable

        Returns
        -------
        None
        """
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
        """
        Deletes all variables from the table.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope", "direction"])

    def get_memory_direction(self,target):
        """
        Returns the memory direction of the target variable.

        Parameters
        ----------
        target : str
            the name of the variable

        Returns
        -------
        int or str
            the memory direction of the variable or the target itself if it is not found in the table
        """
        try:
            return self.df.loc[self.df["id-name"] == target]["direction"].values[0]
           
        except:
            return target


