# Real-Time Rule Engine for Business Logic Processing

This project provides a real-time rule engine that allows users to dynamically define, combine, and evaluate complex business rules through a RESTful API. Designed for flexible business logic, the engine parses rules into an Abstract Syntax Tree (AST) and supports various comparison and logical operators.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [1. Create Rule](#1-create-rule)
  - [2. Combine Rules](#2-combine-rules)
  - [3. Evaluate Rule](#3-evaluate-rule)
- [Testing](#testing)
- [Example Use Case](#example-use-case)
- [Known Issues](#known-issues)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Features
- **Dynamic Rule Creation**: Supports complex conditions with `AND`, `OR`, `>`, `<`, and `=` operators.
- **AST Generation**: Converts rules into a structured AST for easy parsing and evaluation.
- **Real-Time Evaluation**: Evaluate rules instantly against input data.
- **Error Handling**: Handles invalid conditions and provides detailed error messages.

## Technologies
- **Programming Language**: Python
- **Framework**: Flask
- **Regex Library**: `re` (for parsing rule strings)
- **Database**: MongoDB
- **Testing Tools**: Pytest, Postman (for API testing)

## Project Structure

```
.
├── app.py                  # Main API application
├── rules.py                # Rule parsing and AST generation
├── models.py               # Defines Node structure for AST
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── tests                   # Unit testing scripts
    └── test_rules.py
```

# Rule Engine

## Setup and Installation

### Prerequisites
- Python 3.8+
- MongoDB (for data storage)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rule-engine.git
   cd rule-engine
2. **Install required packages:
   ```bash
    pip install -r requirements.txt

3. **Configure MongoDB:

- Set up a local or cloud MongoDB instance.
- Update the MongoDB connection URI in app.py if necessary.
  
4. **Run the application:
   ```bash
    python app.py
## Usage

### 1. Create Rule

- **Endpoint:** `POST /create_rule`
- **Description:** Accepts a rule string and returns the corresponding Abstract Syntax Tree (AST) structure.

#### Request Body:

  ```
     {
    "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience 
     > 5)"
   }
```
Response

```json
{
    "AST": {
        "node_type": "operator",
        "operator": "AND",
        "left": {
            "node_type": "operator",
            "operator": "OR",
            "left": {
                "node_type": "operator",
                "operator": "AND",
                "left": {
                    "node_type": "operand",
                    "value": "age"
                },
                "right": {
                    "node_type": "operand",
                    "value": "Sales"
                }
            },
            "right": {
                "node_type": "operator",
                "operator": "AND",
                "left": {
                    "node_type": "operand",
                    "value": "age"
                },
                "right": {
                    "node_type": "operand",
                    "value": "Marketing"
                }
            }
        },
        "right": {
            "node_type": "operator",
            "operator": "OR",
            "left": {
                "node_type": "operator",
                "operator": ">",
                "left": {
                    "node_type": "operand",
                    "value": "salary"
                },
                "right": {
                    "node_type": "operand",
                    "value": "50000"
                }
            },
            "right": {
                "node_type": "operator",
                "operator": ">",
                "left": {
                    "node_type": "operand",
                    "value": "experience"
                },
                "right": {
                    "node_type": "operand",
                    "value": "5"
                }
            }
        }
    }
}

```
### 2. Combine Rules
- **Endpoint**: `POST /combine_rules`
- **Description**: `Combines multiple rule strings into a single AST structure.`

Request Body:
```
{
    "rules": [
        "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
        "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
    ]
}
```
Response:

```
{
    "combined_AST": { "node_type": "operator", ... }
}
```
### 3. Evaluate Rule
- **Endpoint**: `POST /evaluate_rule`
- **Description**: `Evaluates the AST against input data.`
```
```
Request Body:

```
{
    "ast": { "node_type": "operator", ... },
    "data": {
        "age": 35,
        "department": "Sales",
        "salary": 60000,
        "experience": 6
    }
}
```
Response:
```
{
    "result": true
}
```

# Testing

To run tests, use the following command:


## Testing includes:

- Rule parsing and AST creation.
- Evaluation of rules against test data.
- Error handling for invalid inputs.

## Example Use Case

A real-world example for this rule engine could be an e-commerce platform that determines discount eligibility based on user profile data, such as age, department, salary, or experience level.

## Known Issues

- **Complex Nested Rules**: Very deeply nested rules may create a complex AST, affecting performance.
- **Validation**: Ensure data types match expected operand types, e.g., age as integer.

## Future Enhancements

- **User Interface**: Develop a web-based UI for easier rule creation.
- **Performance Optimization**: Implement caching for frequently used rules.

## License
- **This project is licensed under the MIT License - see the LICENSE file for details.**


- **This README file can be directly added to your GitHub repository in Markdown format, giving a clean, professional presentation of the project. Let me know if you’d like any additional sections!**



