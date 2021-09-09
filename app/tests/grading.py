import unittest

from ..algorithm import grading_function


class TestGradingFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use grading_function() to check your algorithm works
    as it should.
    """

    def test_no_tolerance_correct(self):
        body = {"response": [1, 2], "answer": [1, 2]}

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)

    def test_no_tolerance_incorrect(self):
        body = {"response": [1, 2], "answer": [1, 2.1]}

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), False)

    def test_atol_correct(self):
        body = {
            "response": [1, 2],
            "answer": [1, 2.1],
            "params": {"atol": 0.12},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)

    def test_atol_incorrect(self):
        body = {
            "response": [1, 2],
            "answer": [1, 2.2],
            "params": {"atol": 0.12},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), False)

    def test_rtol_correct(self):
        body = {
            "response": [1, 1.91],
            "answer": [1, 2],
            "params": {"atol": 0.1},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)

    def test_rtol_incorrect(self):
        body = {
            "response": [1, 1.8],
            "answer": [1, 2],
            "params": {"atol": 0.1},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), False)

    def test_2D_correct(self):
        body = {
            "response": [[1, 1], [1, 1]],
            "answer": [[1, 1], [1, 1]],
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)

    def test_2D_incorrect(self):
        body = {
            "response": [[1, 1], [1, 1]],
            "answer": [[1, 1], [1, 0]],
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), False)

    def test_3D_correct(self):
        body = {
            "response": [[[1, 1], [2, 1]], [[2, 1.2], [2, 2]]],
            "answer": [[[1, 1], [2, 1.1]], [[2, 1], [2, 2]]],
            "params": {"atol": 1},
        }

        response = grading_function(body)

        self.assertEqual(response.get("is_correct"), True)

    def test_invalid_shape_user(self):
        body = {
            "response": [1, [1, 1]],
            "answer": [[1, 1], [1, 1]],
        }

        response = grading_function(body)

        self.assertEqual(response.get("error", {}).get("culprit"), "user")

    def test_invalid_shape_author(self):
        body = {
            "response": [[1.2, 1], [1, 2]],
            "answer": [1, [1, 2]],
            "params": {"atol": 3},
        }

        response = grading_function(body)

        self.assertEqual(response.get("error", {}).get("culprit"), "author")


if __name__ == "__main__":
    unittest.main()
