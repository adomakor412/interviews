"""
File: expressiontree.py

Defines nodes for expression trees.
"""

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self._data = data

    def value(self):
        # Exercise
        return 0
      
    def prefix(self):
        # Exercise
        return ""

    def infix(self):
        # Exercise
        return ""

    def postfix(self):
        return str(self)

    def __str__(self):
        return str(self._data)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self.operator = op
        self.leftOperand = leftOper
        self.rightOperand = rightOper

    def value(self):
        # Exercise
        return 0

    def prefix(self):
        # Exercise
        return ""

    def infix(self):
        # Exercise
        return ""
    
    def postfix(self):
        return self.leftOperand.postfix() + " " + \
               self.rightOperand.postfix() + " " + \
               str(self.operator)

def main():
    a = LeafNode(4)
    b = InteriorNode('+', LeafNode(2), LeafNode(3))
    c = InteriorNode('*', a, b)
    c = InteriorNode('^', c, b) 
    print("Expect ((4 * (2 + 3) ^ (2 + 3)):", c.infix())
    print("Expect ^ * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + ^       :", c.postfix())
    print("Expect 3200000                 :", c.value())

if __name__ == "__main__":
    main()



