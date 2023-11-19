import unittest
from my_module.main import make_request

class TestMain(unittest.TestCase):

    def test_make_request(self):
        status_code = make_request()
        self.assertEqual(status_code, 200)

if __name__ == '__main__':
    unittest.main()
