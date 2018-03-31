import os
import json
import unittest
from handler import increment

os.environ['DYNAMO_TABLE'] = 'users_table'

class TestHandler (unittest.TestCase):
    def test_increment (self):
        try:
            event = {}
            with open('./fixtures/increment-event.json') as fixture:
                event = json.load(fixture)
            context = {}

            result = increment(event, context)

            self.assertIn('statusCode', result, 'Status code missing')
            self.assertEqual(result['statusCode'], 200, 'Status code not 200')
        except BaseException as e:
            self.fail(f'Increment failed with `{e}`')

if __name__ == '__main__':
    unittest.main()
