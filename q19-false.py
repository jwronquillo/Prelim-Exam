import unittest

def check():
    name = 'PEDRO'
    return name

class q19(unittest.TestCase):
    def test(self):
        self.assertEqual(check(), 'James')

if __name__ == "__main__":
    unittest.main()