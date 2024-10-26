# from flask import Flask, request, jsonify
# from backend.rules import create_rule, combine_rules, evaluate_rule
# from backend.database import load_rules, save_rules  # Adjust based on actual file structure
# from backend.models import Node  # Import the Node class to help reconstruct the AST

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def home():
#     """Home page endpoint."""
#     return jsonify({"message": "Welcome to the Rule Engine API!"}), 200

# @app.route('/create_rule', methods=['POST'])
# def api_create_rule():
#     """Endpoint to create a rule and return its AST representation."""
#     rule_string = request.json.get('rule_string')
    
#     if not rule_string:
#         return jsonify({"error": "No rule string provided"}), 400
    
#     try:
#         ast = create_rule(rule_string)
#         return jsonify(ast.to_dict()), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/combine_rules', methods=['POST'])
# def api_combine_rules():
#     """Endpoint to combine multiple rules into a single AST."""
#     rules = request.json.get('rules')
    
#     if not rules or not isinstance(rules, list):
#         return jsonify({"error": "Invalid rules provided"}), 400
    
#     try:
#         combined_ast = combine_rules(rules)
#         return jsonify(combined_ast.to_dict()), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/evaluate_rule', methods=['POST'])
# def api_evaluate_rule():
#     """Endpoint to evaluate the AST against provided data."""
#     ast_data = request.json.get('ast')
#     data = request.json.get('data')
    
#     if ast_data is None or data is None:
#         return jsonify({"error": "AST and data must be provided"}), 400
    
#     try:
#         # Reconstruct the AST from the provided ast_data
#         ast_root = reconstruct_ast(ast_data)
#         result = ast_root.evaluate(data)
#         return jsonify({"result": result}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# def reconstruct_ast(ast_dict):
#     """Recursively reconstruct the AST from a dictionary."""
#     if ast_dict is None:
#         return None
    
#     node_type = ast_dict.get('type')
#     value = ast_dict.get('value')
#     left = reconstruct_ast(ast_dict.get('left'))
#     right = reconstruct_ast(ast_dict.get('right'))

#     return Node(node_type, left=left, right=right, value=value)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify
from backend.rules import create_rule, combine_rules, evaluate_rule
from backend.models import Node  # Ensure correct import for Node

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Rule Engine API!"}), 200

@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json.get('rule_string')
    
    if not rule_string:
        return jsonify({"error": "No rule string provided"}), 400
    
    try:
        ast = create_rule(rule_string)
        if ast is None:  # Check for None before calling to_dict()
            return jsonify({"error": "Failed to create AST from rule string"}), 500
        return jsonify(ast.to_dict()), 200
    except Exception as e:
        return jsonify({"error aa rha hai": str(e)}), 500

@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json.get('rules')
    
    if not rules or not isinstance(rules, list):
        return jsonify({"error": "Invalid rules provided"}), 400
    
    try:
        combined_ast = combine_rules(rules)
        if combined_ast is None:  # Check for None before calling to_dict()
            return jsonify({"error": "Failed to combine rules into AST"}), 500
        return jsonify(combined_ast.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    ast_data = request.json.get('ast')
    data = request.json.get('data')
    
    if ast_data is None or data is None:
        return jsonify({"error": "AST and data must be provided"}), 400
    
    try:
        ast_root = reconstruct_ast(ast_data)
        if ast_root is None:  # Check for None
            return jsonify({"error": "Invalid AST provided"}), 400
        result = ast_root.evaluate(data)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def reconstruct_ast(ast_dict):
    if ast_dict is None:
        return None
    
    node_type = ast_dict.get('type')
    value = ast_dict.get('value')
    left = reconstruct_ast(ast_dict.get('left'))
    right = reconstruct_ast(ast_dict.get('right'))

    return Node(node_type, left=left, right=right, value=value)







if __name__ == '__main__':
    app.run(debug=True)
