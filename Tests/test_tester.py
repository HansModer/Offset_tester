import unittest
from offset_tester.tester import OffsetTester
from offset_tester.exceptions import OffsetOutOfBoundsError

class TestOffsetTester(unittest.TestCase):
    def setUp(self):
        self.tester = OffsetTester(buffer_size=100)

    def test_valid_write_and_read(self):
        self.tester.write_at_offset(10, b'hello')
        result = self.tester.read_at_offset(10, 5)
        self.assertEqual(result, b'hello')

    def test_out_of_bounds_write(self):
        with self.assertRaises(OffsetOutOfBoundsError):
            self.tester.write_at_offset(95, b'overflow')

    def test_out_of_bounds_read(self):
        with self.assertRaises(OffsetOutOfBoundsError):
            self.tester.read_at_offset(95, 10)
