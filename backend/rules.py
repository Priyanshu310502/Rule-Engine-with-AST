# # backend/rules.py

# import json
# import re
# from .models import Node

# def parse_condition(condition):
#     """Parse a single condition into an AST node."""
#     if '>' in condition:
#         parts = condition.split('>')
#         return Node(type='operand', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()))
#     elif '<' in condition:
#         parts = condition.split('<')
#         return Node(type='operand', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()))
#     elif '=' in condition:
#         parts = condition.split('=')
#         return Node(type='operand', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()))
#     else:
#         raise ValueError("Invalid condition")

# # def create_rule(rule_string):
# #     """Create an AST from a rule string."""
# #     # Replace logical operators with a recognizable format
# #     rule_string = rule_string.replace('AND', '&&').replace('OR', '||')
    
# #     # Split the rule string into tokens (this is a simplistic approach)
# #     tokens = rule_string.split()
# #     stack = []

# #     for token in tokens:
# #         if token in ['&&', '||']:
# #             right = stack.pop() if stack else None
# #             left = stack.pop() if stack else None
# #             stack.append(Node(type='operator', value=token, left=left, right=right))
# #         else:
# #             stack.append(parse_condition(token))
    
# #     return stack[0] if stack else None



# def create_rule(rule_string):
#     # Basic regex patterns for parsing
#     pattern = r"(\(\s*(.*?)\s*\))|(\w+)\s*([<>=!]+)\s*(\d+|'[^']+')"
    
#     # Replace operators with explicit AND/OR for simplicity
#     rule_string = rule_string.replace("AND", " and ").replace("OR", " or ")

#     # A stack to hold nodes
#     stack = []
    
#     # Simple parser to convert rule_string to AST
#     for match in re.finditer(pattern, rule_string):
#         if match.group(1):  # If it's a parenthesis
#             continue
#         left_operand = match.group(3)
#         operator = match.group(4)
#         right_operand = match.group(5)

#         # Create operand nodes
#         left_node = Node("operand", value=left_operand)
#         right_node = Node("operand", value=right_operand)

#         # Create operator node
#         operator_node = Node("operator", left=left_node, right=right_node)

#         # Push to stack
#         stack.append(operator_node)

#     if not stack:
#         return None  # or raise an exception if no valid nodes were created
    
#     # Return the root node of the AST
#     return stack[-1]


# def combine_rules(rules):
#     """Combine multiple rule strings into a single AST."""
#     combined_ast = None

#     for rule in rules:
#         ast = create_rule(rule)
#         if combined_ast is None:
#             combined_ast = ast
#         else:
#             combined_ast = Node(type='operator', value='&&', left=combined_ast, right=ast)  # Combine with AND
    
#     return combined_ast

# def evaluate_rule(ast_root, data):
#     """Evaluate the AST against the provided data."""
#     if ast_root is None:
#         return False
    
#     if ast_root.type == "operand":
#         left_value = data.get(ast_root.left.value.strip(), None)
#         right_value = ast_root.right.value.strip()
        
#         # Perform comparison based on the operator type
#         if isinstance(left_value, (int, float)):
#             right_value = int(right_value) if right_value.isdigit() else right_value.strip()
#             if right_value.isdigit():
#                 return left_value > int(right_value)
#             else:
#                 return left_value == right_value  # For equality comparison
        
#         return False
    
#     elif ast_root.type == "operator":
#         if ast_root.value == '&&':
#             return evaluate_rule(ast_root.left, data) and evaluate_rule(ast_root.right, data)
#         elif ast_root.value == '||':
#             return evaluate_rule(ast_root.left, data) or evaluate_rule(ast_root.right, data)
    
#     return False








# # backend/rules.py

# # backend/rules.py

# import re
# from .models import Node

# def parse_condition(condition):
#     """Parse a single condition into an AST node."""
#     condition = condition.strip()

#     # Match comparisons and split
#     if '>' in condition:
#         parts = condition.split('>')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='>')
#     elif '<' in condition:
#         parts = condition.split('<')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='<')
#     elif '=' in condition:
#         parts = condition.split('=')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='=')
#     else:
#         raise ValueError("Invalid condition")

# def create_rule(rule_string):
#     """Create an AST from a rule string."""
#     # Normalize the rule string for parsing
#     rule_string = rule_string.replace('AND', '&&').replace('OR', '||')

#     # Tokenize the input string using regex
#     tokens = re.findall(r'\(|\)|\w+|\S+', rule_string)  # Get words and operators
#     stack = []
#     output = []

#     precedence = {'&&': 1, '||': 0}

#     # Shunting-yard algorithm for parsing
#     for token in tokens:
#         token = token.strip()
#         if token in precedence:  # If the token is an operator
#             while (stack and stack[-1] in precedence and 
#                    precedence[stack[-1]] >= precedence[token]):
#                 output.append(stack.pop())
#             stack.append(token)
#         elif token == '(':
#             stack.append(token)
#         elif token == ')':
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             stack.pop()  # Remove the '('
#         else:
#             output.append(token)  # Append operand

#     while stack:
#         output.append(stack.pop())

#     # Now create the AST from the output
#     ast_stack = []

#     for token in output:
#         if token in ['&&', '||']:
#             right = ast_stack.pop() if ast_stack else None
#             left = ast_stack.pop() if ast_stack else None
#             ast_stack.append(Node(type='operator', value=token, left=left, right=right))
#         else:
#             ast_stack.append(parse_condition(token))

#     return ast_stack[0] if ast_stack else None

# def combine_rules(rules):
#     """Combine multiple rule strings into a single AST."""
#     combined_ast = None

#     for rule in rules:
#         ast = create_rule(rule)
#         if combined_ast is None:
#             combined_ast = ast
#         else:
#             combined_ast = Node(type='operator', value='&&', left=combined_ast, right=ast)  # Combine with AND

#     return combined_ast

# def evaluate_rule(ast_root, data):
#     """Evaluate the AST against the provided data."""
#     if ast_root is None:
#         return False

#     if ast_root.type == "operand":
#         return data.get(ast_root.value.strip(), None)

#     elif ast_root.type == "operator":
#         left_eval = evaluate_rule(ast_root.left, data) if ast_root.left else None
#         right_eval = evaluate_rule(ast_root.right, data) if ast_root.right else None
        
#         if ast_root.value == '>':
#             return left_eval > right_eval
#         elif ast_root.value == '<':
#             return left_eval < right_eval
#         elif ast_root.value == '=':
#             return left_eval == right_eval
#         elif ast_root.value == '&&':
#             return left_eval and right_eval
#         elif ast_root.value == '||':
#             return left_eval or right_eval

#     return False







# import re
# from .models import Node

# def parse_condition(condition):
#     """Parse a single condition into an AST node."""
#     condition = condition.strip()

#     # Match comparisons and split
#     if '>' in condition:
#         parts = condition.split('>')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='>')
#     elif '<' in condition:
#         parts = condition.split('<')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='<')
#     elif '=' in condition:
#         parts = condition.split('=')
#         return Node(type='operator', left=Node(type='operand', value=parts[0].strip()), 
#                     right=Node(type='operand', value=parts[1].strip()), value='==')  # Use '==' for equality
#     else:
#         raise ValueError(f"Invalid condition: {condition}")  # Provide more context in the error message

# def create_rule(rule_string):
#     """Create an AST from a rule string."""
#     # Normalize the rule string for parsing
#     rule_string = rule_string.replace('AND', '&&').replace('OR', '||')

#     # Tokenize the input string using regex
#     tokens = re.findall(r'\(|\)|\w+\s*([<>=!]+)\s*\w+|(\S+)', rule_string)  # Get words and operators
#     stack = []
#     output = []

#     precedence = {'&&': 1, '||': 0}

#     # Shunting-yard algorithm for parsing
#     for token in tokens:
#         if isinstance(token, tuple):
#             condition = token[0] or token[1]
#             if condition:
#                 output.append(condition)  # Append operand
#         else:
#             token = token.strip()
#             if token in precedence:  # If the token is an operator
#                 while (stack and stack[-1] in precedence and 
#                        precedence[stack[-1]] >= precedence[token]):
#                     output.append(stack.pop())
#                 stack.append(token)
#             elif token == '(':
#                 stack.append(token)
#             elif token == ')':
#                 while stack and stack[-1] != '(':
#                     output.append(stack.pop())
#                 stack.pop()  # Remove the '('

#     while stack:
#         output.append(stack.pop())

#     # Now create the AST from the output
#     ast_stack = []

#     for token in output:
#         if token in ['&&', '||']:
#             right = ast_stack.pop() if ast_stack else None
#             left = ast_stack.pop() if ast_stack else None
#             ast_stack.append(Node(type='operator', value=token, left=left, right=right))
#         else:
#             # Check for complete conditions before parsing
#             condition = token.strip()
#             if condition:
#                 ast_stack.append(parse_condition(condition))

#     return ast_stack[0] if ast_stack else None

# def combine_rules(rules):
#     """Combine multiple rule strings into a single AST."""
#     combined_ast = None

#     for rule in rules:
#         ast = create_rule(rule)
#         if combined_ast is None:
#             combined_ast = ast
#         else:
#             combined_ast = Node(type='operator', value='&&', left=combined_ast, right=ast)  # Combine with AND

#     return combined_ast

# def evaluate_rule(ast_root, data):
#     """Evaluate the AST against the provided data."""
#     if ast_root is None:
#         return False

#     if ast_root.type == "operand":
#         return data.get(ast_root.value.strip(), None)

#     elif ast_root.type == "operator":
#         left_eval = evaluate_rule(ast_root.left, data) if ast_root.left else None
#         right_eval = evaluate_rule(ast_root.right, data) if ast_root.right else None
        
#         if ast_root.value == '>':
#             return left_eval > right_eval
#         elif ast_root.value == '<':
#             return left_eval < right_eval
#         elif ast_root.value == '==':
#             return left_eval == right_eval
#         elif ast_root.value == '&&':
#             return left_eval and right_eval
#         elif ast_root.value == '||':
#             return left_eval or right_eval

#     return False



import re
from .models import Node

def parse_condition(condition):
    """Parse a single condition into an AST node."""
    condition = condition.strip()

    # Match comparisons and split
    if '>' in condition:
        parts = condition.split('>')
        return Node(node_type='operator', 
                    left=Node(node_type='operand', value=parts[0].strip()), 
                    right=Node(node_type='operand', value=parts[1].strip()), 
                    value='>')
    elif '<' in condition:
        parts = condition.split('<')
        return Node(node_type='operator', 
                    left=Node(node_type='operand', value=parts[0].strip()), 
                    right=Node(node_type='operand', value=parts[1].strip()), 
                    value='<')
    elif '=' in condition:
        parts = condition.split('=')
        return Node(node_type='operator', 
                    left=Node(node_type='operand', value=parts[0].strip()), 
                    right=Node(node_type='operand', value=parts[1].strip()), 
                    value='==')  # Use '==' for equality
    else:
        # Check for string comparisons with '==' 
        if '==' in condition:
            parts = condition.split('==')
            return Node(node_type='operator', 
                        left=Node(node_type='operand', value=parts[0].strip()), 
                        right=Node(node_type='operand', value=parts[1].strip()), 
                        value='==')  # Use '==' for equality
        else:
            raise ValueError(f"Invalid condition: {condition}")

def create_rule(rule_string):
    """Create an AST from a rule string."""
    # Normalize the rule string for parsing
    rule_string = rule_string.replace('AND', '&&').replace('OR', '||')

    # Tokenize the input string using regex
    tokens = re.findall(r'\(|\)|\w+\s*([<>=!]+)\s*\w+|(\S+)', rule_string)
    stack = []
    output = []

    precedence = {'&&': 1, '||': 0}

    # Shunting-yard algorithm for parsing
    for token in tokens:
        if isinstance(token, tuple):
            condition = token[0] or token[1]
            if condition:
                output.append(condition)
        else:
            token = token.strip()
            if token in precedence:  # If the token is an operator
                while (stack and stack[-1] in precedence and 
                       precedence[stack[-1]] >= precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the '('

    while stack:
        output.append(stack.pop())

    # Now create the AST from the output
    ast_stack = []

    for token in output:
        if token in ['&&', '||']:
            right = ast_stack.pop() if ast_stack else None
            left = ast_stack.pop() if ast_stack else None
            ast_stack.append(Node(node_type='operator', value=token, left=left, right=right))
        else:
            condition = token.strip()
            if condition:
                ast_stack.append(parse_condition(condition))

    return ast_stack[0] if ast_stack else None

def combine_rules(rules):
    """Combine multiple rule strings into a single AST."""
    combined_ast = None

    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node(node_type='operator', value='&&', left=combined_ast, right=ast)  # Combine with AND

    return combined_ast

def evaluate_rule(ast_root, data):
    """Evaluate the AST against the provided data."""
    if ast_root is None:
        return False

    if ast_root.node_type == "operand":
        return data.get(ast_root.value.strip(), None)

    elif ast_root.node_type == "operator":
        left_eval = evaluate_rule(ast_root.left, data) if ast_root.left else None
        right_eval = evaluate_rule(ast_root.right, data) if ast_root.right else None
        
        if ast_root.value == '>':
            return left_eval > right_eval
        elif ast_root.value == '<':
            return left_eval < right_eval
        elif ast_root.value == '==':
            return left_eval == right_eval
        elif ast_root.value == '&&':
            return left_eval and right_eval
        elif ast_root.value == '||':
            return left_eval or right_eval

    return False
