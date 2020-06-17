import unittest
import validate_input_in_functions

class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(validate_input_in_functions.score_input("math"), "math: 0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate_input_in_functions.score_input("math", 92), "math: 92")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate_input_in_functions.score_input("math", -92), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(validate_input_in_functions.score_input("math", 192), "Invalid test score, try again!")

    def test_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            validate_input_in_functions.score_input("math", "math")

    def test_score_input_invalid_message(self):
        self.assertEqual(validate_input_in_functions.score_input("math", 92, "Invalid test score, try again!"), "math: 92")

if __name__ == '__main__':
    unittest.main()
