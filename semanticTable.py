import pandas as pd

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
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope"])

    def add_var(self, id_name, var_type, value=None, scope="Global"):
        if id_name in self.df["id-name"].values:
            raise ValueError(f"Error: Multiple declaration of {id_name}")
        self.df.loc[len(self.df)] = [id_name, var_type, value, scope]

    def delete(self):
        self.df = pd.DataFrame(columns=["id-name", "type", "value", "scope"])
