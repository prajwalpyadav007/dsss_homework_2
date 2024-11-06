import unittest
from math_quiz import generate_integers, generate_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_generate_integers(self):
        # Test specified boundary conditions within a specified range
        for _ in range(100): 
            result= generate_integers(1,10)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result,10)

    def test_generate_operator(self):
        #check the operator is within the specified choices
        operators={'+','-','*'}
        for _ in range(50):
            result=generate_operator()
            self.assertIn(result,operators)
        

    def test_generate_problem(self):
        #test addition
        problem, answer = generate_problem(3,4,'+')
        self.assertEqual(problem,"3 + 4")
        self.assertEqual(answer, 7)

        #test subtarction
        problem, answer = generate_problem(10,4,'-')
        self.assertEqual(problem,"10 - 4")
        self.assertEqual(answer, 6) 

        #test multiplication
        problem, answer = generate_problem(2,5,'*')
        self.assertEqual(problem,"2 * 5")
        self.assertEqual(answer, 10)         

if __name__ == "__main__":
    unittest.main()
