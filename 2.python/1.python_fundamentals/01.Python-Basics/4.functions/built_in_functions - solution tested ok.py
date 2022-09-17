from math import pi

string = "Hello world!"
count_alpha = len(string)
print(count_alpha)
count_float = float(count_alpha)
print(count_float)
round_pi = round(pi,2)
print(round_pi)
reversed_text = string[::-1]
reversed_text = [*reversed_text]
print(reversed_text)
print(type(reversed_text))
age = input("Enter age: ")
num = [2, 8, 1, 4, 6, 3, 7]
sorted_num = num.copy();sorted_num.sort()
sum_of_list = sum(num)
min_value = min(num)
max_value = max(num)
calc = "1 + 2"
string_interpret = eval(calc)


import unittest


class TestNotebook(unittest.TestCase):
    def test_count_alpha(self):
        self.assertEqual(count_alpha, 12)

    def test_count_float(self):
        self.assertEqual(type(count_float), float)

    def test_pi(self):
        self.assertEqual(3.14, round_pi)

    def test_reversed(self):
        self.assertEqual(
            reversed_text, ["!", "d", "l", "r", "o", "w", " ", "o", "l", "l", "e", "H"]
        )

    def test_age(self):
        self.assertEqual(type(age), str)

    def test_sorted(self):
        self.assertEqual(sorted_num, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sum_of_list, 31)

    def test_min(self):
        self.assertEqual(min_value, 1)

    def test_max(self):
        self.assertEqual(max_value, 8)

    def test_interpret(self):
        self.assertEqual(string_interpret, 3)


unittest.main(argv=[""], verbosity=2, exit=False)
