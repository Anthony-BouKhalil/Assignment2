import unittest

class TestSum(unittest.TestCase):
    
    def test_response1(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == '__main__':
        unittest.main()
        
