from app import calc

from django.test import SimpleTestCase


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        x = 2
        y = 3
        res = calc.add(x, y)
        self.assertEqual(res, 5)
