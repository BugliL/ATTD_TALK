import unittest

def uppercase(string: str) -> str:
    return string.upper()


class UppercaseTestFunctionShould(unittest.TestCase):

    def test_return_uppercase_string_given_string(self):
        self.assertEqual(uppercase(string='foo'), 'FOO')

