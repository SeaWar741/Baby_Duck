# **Baby Duck Programming Language**

![alt text](/public/img/babyDuck.png)

Baby_Duck is an imperative and procedural programming language designed for teaching fundamental concepts of compiling and executing programs. This micro-language allows users to become familiar with the structure and control flow of classic programming languages, providing a simplified environment for learning basic syntax and semantics.


### **Requirments:**
- Python >= 3.9.18
- ANTLR

```bash
pip install -r requirements.txt
```

### **Generate files with ANTLR:**
```bash
antlr4 -Dlanguage=Python3 -visitor -o utils BabyDuck.g4
```

### **Run code:**
```bash
python baby_duck.py ./testing/test.babyduck 
```

To execute it in **debugging mode**:
```bash
python baby_duck.py ./testing/test.babyduck --debug
```

This will display the quadruples in plain operations, memory operations, operand stacks, temporal values, and directions, as well as function tables, variable tables, among other miscellaneous debugging functionalities.
