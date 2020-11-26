import unittest
from solution import CodingQuiz
import time
  
class TestCodingQuiz(unittest.TestCase): 
      
    def setUp(self): 
        auth_token='LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF'
        self.cq_obj = CodingQuiz(auth_token)
        self.endpoint = 'https://atlas.pretio.in/atlas/coding_quiz'
  
    def test_status_429(self):
        status_code = self.cq_obj.make_call(self.endpoint)
        self.assertEqual(429, status_code) 

    def test_status_500(self):         
        status_code = self.cq_obj.make_call(self.endpoint)
        self.assertEqual(500, status_code) 
  
if __name__ == '__main__': 
    unittest.main() 