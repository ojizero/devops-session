import unittest
import handler

class MyTests(unittest.TestCase):
    def test_increment (self):
        response = handler.increment({}, {})

        self.assertEqual(response['statusCode'], 200, 'must return HTTP success')


if __name__ == '__main__':
    unittest.main()
