import pandas as pd

class SemanticTable:
    def __init__(self):
        # Functions Directory
        func_columns = ['Function Name', 'Return Type', 'Parameters', 'Var-table']
        self.functions_directory = pd.DataFrame(columns=func_columns)

        # Global Var-table
        var_columns = ['Variable Name', 'Type', 'Value', 'Scope']
        self.global_var_table = pd.DataFrame(columns=var_columns)

    def add_function(self, name, return_type, parameters):
        local_var_table = pd.DataFrame(columns=self.global_var_table.columns)  # Each function gets its own Var-table
        new_function = pd.DataFrame({
            'Function Name': [name],
            'Return Type': [return_type],
            'Parameters': [parameters],
            'Var-table': [local_var_table]
        })
        self.functions_directory = pd.concat([self.functions_directory, new_function], ignore_index=True)

    def add_global_var(self, name, type, value):
        new_var = pd.DataFrame({
            'Variable Name': [name],
            'Type': [type],
            'Value': [value],
            'Scope': ['Global']
        })
        self.global_var_table = pd.concat([self.global_var_table, new_var], ignore_index=True)

    def add_local_var(self, name, type, value, scope):
        local_var_table = self.functions_directory.loc[self.functions_directory['Function Name'] == scope, 'Var-table'].iloc[0]
        new_var = pd.DataFrame({
            'Variable Name': [name],
            'Type': [type],
            'Value': [value],
            'Scope': [scope]
        })
        updated_var_table = pd.concat([local_var_table, new_var], ignore_index=True)
        # Update the Var-table in the functions_directory
        self.functions_directory.loc[self.functions_directory['Function Name'] == scope, 'Var-table'] = [updated_var_table]

    def search_global_var(self, name):
        return self.global_var_table.loc[self.global_var_table['Variable Name'] == name]

    def search_local_var(self, name, scope):
        local_var_table = self.functions_directory.loc[self.functions_directory['Function Name'] == scope, 'Var-table'].iloc[0]
        return local_var_table.loc[local_var_table['Variable Name'] == name]

    def search_function(self, name):
        return self.functions_directory.loc[self.functions_directory['Function Name'] == name]
