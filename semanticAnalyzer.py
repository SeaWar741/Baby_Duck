class SemanticAnalyzer:
    ERROR = "ERROR"
    
    def __init__(self):
        # Cubo semántico
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
        
        # Pilas y estructuras de control
        self.PilaO = []
        self.PTypes = []
        self.POper = []
        self.Quads = []
        self.AVAIL = {"next": 1000}
    
    def generate_quad(self, operator, left_operand, right_operand):
        result = self.AVAIL["next"]
        self.AVAIL["next"] += 1
        quad = (operator, left_operand, right_operand, result)
        self.Quads.append(quad)
        return result
    
    def process_operation(self, operators):
        if self.POper and self.POper[-1] in operators:
            right_operand = self.PilaO.pop()
            right_type = self.PTypes.pop()
            left_operand = self.PilaO.pop()
            left_type = self.PTypes.pop()
            operator = self.POper.pop()
            
            result_type = self.Semantics[left_type][right_type].get(operator, self.ERROR)
            if result_type != self.ERROR:
                result = self.generate_quad(operator, left_operand, right_operand)
                self.PilaO.append(result)
                self.PTypes.append(result_type)
            else:
                raise Exception("Type mismatch")
            
# Ejemplo de uso
""" analyzer = SemanticAnalyzer()

analyzer.PilaO.append("variable1")
analyzer.PTypes.append("int")
analyzer.POper.append("+")

analyzer.PilaO.append("variable2")
analyzer.PTypes.append("int")

analyzer.process_operation(['+', '-'])

print(analyzer.Quads) """