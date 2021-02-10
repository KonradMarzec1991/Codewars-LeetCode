from math import sqrt
import unittest


def sol_equa(n):
    if not isinstance(n, int) or n < 0:
        return []

    results = []
    for sqr in range(1, int(sqrt(n)) + 1):
        if n % sqr == 0:
            y = (n - sqr*sqr)/(4*sqr)
            x = sqr + 2*y

            if y == int(y) and x == int(x):
                results.append([int(x), int(y)])

    results.sort(key=lambda a: a[0], reverse=True)
    return results


class DiophantineTest(unittest.TestCase):

    def test_diophantine_valid(self):
        self.assertListEqual(sol_equa(12), [[4, 1]])
        self.assertListEqual(sol_equa(13), [[7, 3]])
        self.assertListEqual(sol_equa(16), [[4, 0]])
        self.assertListEqual(sol_equa(17), [[9, 4]])

    def test_diophantine_invalid(self):
        self.assertListEqual(sol_equa(-10), [])
        self.assertListEqual(sol_equa(14), [])
        self.assertListEqual(sol_equa('aaa'), [])


if __name__ == '__main__':
    unittest.main()