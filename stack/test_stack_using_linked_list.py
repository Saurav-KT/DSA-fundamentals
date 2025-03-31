import unittest
from stack_using_linked_list import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_peek_empty_stack_raises_error(self):
        with self.assertRaises(IndexError) as context:
            self.stack.peek()
        self.assertEqual(str(context.exception), "peek from empty stack")

    def test_pop_empty_stack_raises_error(self):
        with self.assertRaises(IndexError)as context:
            self.stack.pop()
            self.assertEqual(str(context.exception), "pop from empty stack")

    def test_non_empty_stack(self):
            print('Test: One or more element')
            self.stack.push(10)
            self.assertEqual(self.stack.peek(), 10)
            self.assertEqual(self.stack.pop(), 10)
            self.assertTrue(self.stack.is_empty(), True)

            self.stack.push(20)
            self.stack.push(30)
            self.stack.push(40)

            self.assertEqual(self.stack.pop(),40)
            self.assertEqual(self.stack.peek(),30)
            self.assertEqual(self.stack.pop(),30)
            self.assertEqual(self.stack.peek(),20)
            self.assertTrue(self.stack.is_empty(), False)
            self.assertEqual(self.stack.pop(),20)
            self.assertTrue(self.stack.is_empty(),True)

            print('Success: test_end_to_end')

if __name__ == '__main__':
    unittest.main()



