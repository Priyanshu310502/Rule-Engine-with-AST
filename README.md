Real-Time Rule Engine for Business Logic Processing
Overview
This project implements a real-time rule engine that allows users to define, combine, and evaluate business logic rules dynamically. The engine parses rules into Abstract Syntax Trees (ASTs) for efficient processing and supports various operators like AND, OR, greater-than, less-than, and equality.

Features
Dynamic Rule Creation: Define complex rules using logical operators and conditions.
AST Generation: Convert rules into an Abstract Syntax Tree for structured evaluation.
Rule Combination: Combine multiple rules to create compound expressions.
Real-Time Evaluation: Evaluate rules in real-time against user data inputs.
Error Handling: Provides detailed error messages for invalid rules or data formats.
Technologies Used
Python: Core language for backend logic.
Flask: Handles API requests.
re (Regular Expressions): Used for rule parsing.
MongoDB: Database for rule storage and retrieval.
Postman: For testing API endpoints.
Project Structure
bash
Copy code
.
├── app.py                  # Main application script
├── rules.py                # Rule parsing and AST generation
├── models.py               # Node structure for AST
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── tests                   # Contains test cases for various functionalities
    └── test_rules.py
Getting Started
Prerequisites
Python 3.8+
MongoDB for database storage
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/rule-engine.git
cd rule-engine
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Set Up MongoDB

Install and run MongoDB locally or configure it on a cloud service.
Update MongoDB connection string in app.py if necessary.
Run the Application

bash
Copy code
python app.py
Access APIs

The application runs at http://127.0.0.1:5000.
Test the endpoints using Postman or cURL.
Usage
API Endpoints
1. Create Rule
Endpoint: POST /create_rule
Description: Parses a rule string and returns the generated AST.

json
Copy code
Request Body:
{
    "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
}

Response:
{
    "AST": { ... }  # AST structure in JSON format
}
2. Combine Rules
Endpoint: POST /combine_rules
Description: Combines multiple rules into a single AST.

json
Copy code
Request Body:
{
    "rules": [
        "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
        "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    ]
}

Response:
{
    "combined_AST": { ... }  # Combined AST in JSON format
}
3. Evaluate Rule
Endpoint: POST /evaluate_rule
Description: Evaluates a rule against provided data.

json
Copy code
Request Body:
{
    "ast": { ... },  # AST generated from previous endpoint
    "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 6
    }
}

Response:
{
    "result": true  # Evaluation result
}
Testing
Run Tests:

bash
Copy code
pytest tests/
Test Coverage:

Test cases for parsing rules, AST generation, rule combination, and evaluation.
Includes checks for error handling and invalid inputs.
Example Use Case
Consider a scenario where an e-commerce company needs to determine user eligibility for discounts based on multiple criteria. The rule engine evaluates user data against discount rules and returns a result based on eligibility conditions.

Known Issues and Limitations
Nested Expressions: Highly nested rules may result in deeper ASTs, affecting performance.
Condition Validation: Ensure data types match for operands (e.g., numeric values for salary/age).
Future Enhancements
UI for Rule Creation: A user-friendly interface for creating and testing rules.
Caching for Performance: Caching frequently used ASTs to improve evaluation time.
Machine Learning Integration: Enable rule-based learning to adjust conditions dynamically.
License
This project is licensed under the MIT License. See LICENSE for details.

Author
[Your Name] - [Your Contact Information]
