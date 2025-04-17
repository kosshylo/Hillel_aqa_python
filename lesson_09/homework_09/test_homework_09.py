import unittest

from lesson_09.homework_09.mfunc import sum_func, arithmetic_mean, longest_word, sum_numbers_from_string, unic_symbols_func



class TestMyFunctionsUnits(unittest.TestCase):

    def test1_PosSumFunc(self):
        result = sum_func(3.33, 4.44)
        self.assertEqual(7.77, result)

    def test2_NegSumFunc_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_func("3", 4.44)

    def test3_Pos_ArifMean(self):
        input_list: list = [1, 3, 5]
        ar = arithmetic_mean(input_list)
        self.assertEqual(3,ar)

    def test4_Neg_ArifMean_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            arithmetic_mean([])

    def test5_Pos_LongWord(self):
        input_list: list[str] = ["World", "Hello", "Automation"]
        assert "Automation" == longest_word(input_list)

    def test6_Neg_LongWord_wrong_type(self):
        with self.assertRaises(NameError):
            longest_word([1, defv,"4"])

    def test7_Pos_SumNumbersFromString(self):
        self.assertEqual(10,sum_numbers_from_string("1,2,3,4"))

    def test8_SumNumbersFromString_string_with_float(self):
        self.assertEqual("Не можу це зробити!", sum_numbers_from_string("1,2,3.5,4"))

    def test9_Pos_UnicSymbolsMoreThan10(self):
        self.assertTrue(unic_symbols_func("abcdefghijklm"))

    def test_Neg_UnicSymbolsMoreThan10(self):
        self.assertFalse(unic_symbols_func("abcabcabc"))

if __name__ == '__main__':
    unittest.main()