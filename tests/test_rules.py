# tests/test_rules.py

import unittest
from backend.rules import create_rule, combine_rules, evaluate_rule

class TestRules(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age > 30"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

    def test_combine_rules(self):
        rules = ["age > 30", "department = 'Sales'"]
        combined_ast = combine_rules(rules)
        self.assertIsNotNone(combined_ast)

    def test_evaluate_rule(self):
        ast = create_rule("age > 30")
        data = {"age": 35}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
