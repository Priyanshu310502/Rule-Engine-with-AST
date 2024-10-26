# class Node:
#     def __init__(self, node_type, left=None, right=None, value=None):
#         self.type = node_type  # "operator" or "operand"
#         self.left = left       # Reference to left Node
#         self.right = right     # Reference to right Node
#         self.value = value     # Value for operator nodes (e.g., ">", "<", "AND", "OR")

#     def __repr__(self):
#         """Return a string representation of the node for debugging purposes."""
#         if self.type == "operand":
#             return f"Operand(value={self.value})"
#         else:
#             return f"Operator(value={self.value}, left={self.left}, right={self.right})"

#     def to_dict(self):
#         """Convert the Node to a dictionary format for JSON serialization."""
#         if self.type == "operand":
#             return {
#                 "type": self.type,
#                 "value": self.value
#             }
#         else:
#             return {
#                 "type": self.type,
#                 "value": self.value,
#                 "left": self.left.to_dict() if self.left else None,
#                 "right": self.right.to_dict() if self.right else None
#             }

#     def evaluate(self, data):
#         """Evaluate the node's value based on the given data."""
#         if self.type == "operand":
#             # Return the value associated with the operand name from the data
#             return data.get(self.value.strip(), None)

#         elif self.type == "operator":
#             # Evaluate left and right children
#             left_eval = self.left.evaluate(data) if self.left else None
#             right_eval = self.right.evaluate(data) if self.right else None
            
#             # Perform the operation based on the operator type
#             if self.value == '>':
#                 return left_eval > right_eval
#             elif self.value == '<':
#                 return left_eval < right_eval
#             elif self.value == '=':
#                 return left_eval == right_eval
#             elif self.value == '&&':  # Logical AND
#                 return left_eval and right_eval
#             elif self.value == '||':  # Logical OR
#                 return left_eval or right_eval

#         return None



class Node:
    def __init__(self, value=None, left=None, right=None, node_type=None):
        self.value = value
        self.left = left
        self.right = right
        self.node_type = node_type  # Use 'node_type' instead of 'type'

    def to_dict(self):
        return {
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
            'node_type': self.node_type
        }

