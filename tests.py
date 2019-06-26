#!/usr/bin/python3
import random
import string
import unittest
from time import process_time_ns

from get_substring import get_2ch_substring

max_str_len_pow = 18
max_str_len = 2 ** 18
min_str_len_pow = 10
max_c_dev_percent = 15


def generate_random_str(size=2, letters=string.printable):
    """Generate a random string of fixed length """
    return ''.join(random.choice(letters) for i in range(size))


def execution_time_average(probes=1):
    """Measures average execution time of func, calls gen_func() for each probe"""

    def decorator(func):
        def wrapper(gen_func):
            time_acc = 0
            n = 0
            total_probes = 0
            for i in range(probes):
                gen_str = gen_func()
                start_time = process_time_ns()
                # Additional probes to equalize the number of operations
                for j in range(max_str_len // len(gen_str)):
                    func(gen_str)
                    total_probes += 1
                time_acc += process_time_ns() - start_time
                n += len(gen_str)
            n = n // probes
            t = time_acc / total_probes
            return n, total_probes, t

        return wrapper

    return decorator


@execution_time_average(probes=10)
def get_2ch_substring_measure(gen_func):
    return get_2ch_substring(gen_func)


class TestBasicMethods(unittest.TestCase):

    def test_zero_string(self):
        self.assertEqual(get_2ch_substring(''), '')
        self.assertEqual(get_2ch_substring('\0'), '')

    def test_not_string(self):
        for in_str in [None, 1, b'1234', ['1', '2', '3'], {'1': 1}]:
            with self.assertRaises(TypeError):
                get_2ch_substring(in_str)

    def test_one_char_string(self):
        self.assertEqual(get_2ch_substring('a'), 'a')
        self.assertEqual(get_2ch_substring('aa'), 'aa')

    def test_multi_char_string(self):
        self.assertEqual(get_2ch_substring('ab'), 'ab')
        self.assertEqual(get_2ch_substring('aaaabbbb'), 'aaaabbbb')
        self.assertEqual(get_2ch_substring('abababab'), 'abababab')
        self.assertEqual(get_2ch_substring('ababcbaba'), 'abab')
        self.assertEqual(get_2ch_substring('ababccccbaba'), 'bccccb')
        self.assertEqual(get_2ch_substring('ababccbccbaba'), 'bccbccb')
        self.assertEqual(get_2ch_substring('ababcdcdbaba'), 'abab')
        self.assertEqual(get_2ch_substring('aaaabbbbcccc'), 'aaaabbbb')
        self.assertEqual(get_2ch_substring('aaaabbbbccccc'), 'bbbbccccc')
        self.assertEqual(get_2ch_substring('aaaabb\0bbccccc'), 'aaaabb')

    def test_measure_complexity(self):
        """
        Measures average execution time for different lengths of input string.
        At complexity O(N) - the execution time divided by the length of the string should be ~constant
        for any length of string.
        """
        c_arr = []
        c_acc = 0
        for i in range(min_str_len_pow, max_str_len_pow + 1):
            def gen_func():
                return generate_random_str(size=2 ** i, letters=string.digits + string.ascii_letters)

            n, p, t = get_2ch_substring_measure(gen_func)
            c_cur = t / n
            c_arr.append(c_cur)
            c_acc += c_cur
            print(f"N:{n:>8} chars | PROBES: {p:>5} | T(avg):{t:>12.0f} ns | T/N: {c_cur:>8.0f} ns/char")
        # Average T/N value
        c_avg = c_acc / len(c_arr)
        # Deviation
        c_dev = 0
        for i in c_arr:
            c_dev += (c_avg - i) ** 2
        c_dev = (c_dev / len(c_arr)) ** 0.5
        c_dev_percent = (c_dev * 100 / c_avg)

        print(f"T/N(avg):{c_avg:>4.0f}ns/char | T/N(dev):{c_dev:>4.0f}ns/char ~{c_dev_percent:<3.1f}%")
        self.assertLessEqual(c_dev * 100 / c_avg, max_c_dev_percent)


if __name__ == '__main__':
    unittest.main()
