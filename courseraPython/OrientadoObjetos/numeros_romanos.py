import unittest

class RomanNumber(object):
    #estas varibles de clase, se implememtan por el Quinto refactoring
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    def int_to_roman(self, n):
        #return #Si retornamos none el test va a fallar
        #return 'I' #devolviendo el valor el test pasa!
        # if n == 1:
        #     return 'I'
        # elif n == 2:
        #     return 'II'
        # elif n == 3:
        #     return 'III'

        #Primer refactoring al codigo anterior    
        # roman_number = ''
        # for x in range(n):
        #     roman_number += 'I'
        # return roman_number

        #Segundo refactoring
        # roman_number = ''
        # if n == 6:
        #     roman_number = 'VI'
        # elif n == 5:
        #     roman_number = 'V'
        # elif n == 4:
        #     roman_number = 'IV'
        # else:
        #     for x in range(n):
        #         roman_number += 'I'
        # return roman_number

        #Tercer refactoring
        # remaining = n
        # roman_number = ''
        # if remaining >= 9:
        #     roman_number = 'IX'
        #     remaining -= 9
        # if remaining >=5:
        #     roman_number += 'V'
        #     remaining -= 5
        # if remaining >= 4:
        #     roman_number += 'IV'
        #     remaining -= 4
        # for x in range(remaining):
        #     roman_number += 'I'
        # return roman_number

        #Cuarto refactoring, aplicando un Extract Method
        # remaining = n
        # roman_number = ''
        # roman_number, remaining = self.append_roman_number(remaining, 9, 'IX', roman_number)
        # roman_number, remaining = self.append_roman_number(remaining, 5, 'V', roman_number)
        # roman_number, remaining = self.append_roman_number(remaining, 4, 'IV', roman_number)
        # for x in range(remaining):
        #     roman_number += 'I'
        # return roman_number

        #Quinto refactoring
        # remaining = n
        # roman_number = ''
        # for i in range(len(self.values)):
        #     roman_number, remaining = self.append_roman_number(remaining, self.values[i], self.symbols[i], roman_number)
        
        # for x in range(remaining):
        #     roman_number += 'I'
        # return roman_number

        #Sexto refactoring
        remaining = n
        roman_number = ''
        for i in range(len(self.values)):
            roman_number, remaining = self.append_roman_number(remaining, self.values[i], self.symbols[i], roman_number)
        return roman_number

    def append_roman_number(self, n, number, roman_value, roman_number):
        remaining = n
        while remaining >= number:
            roman_number = roman_number + roman_value
            remaining -= number
        
        return roman_number, remaining

class RomanNumberTest(unittest.TestCase):
    def setUp(self):
        self.roman_number = RomanNumber()
    
    def test_one_to_roman(self):
        roman_number = self.roman_number.int_to_roman(1)
        self.assertEqual('I', roman_number)
    
    def test_two_to_roman(self):
        roman_number = self.roman_number.int_to_roman(2)
        self.assertEqual('II', roman_number)
    
    def test_three_to_roman(self):
        roman_number = self.roman_number.int_to_roman(3)
        self.assertEqual('III', roman_number)
    
    def test_four_to_roman(self):
        roman_number = self.roman_number.int_to_roman(4)
        self.assertEqual('IV', roman_number)
    
    def test_five_to_roman(self):
        roman_number = self.roman_number.int_to_roman(5)
        self.assertEqual('V', roman_number)
    
    def test_six_to_roman(self):
        roman_number = self.roman_number.int_to_roman(6)
        self.assertEqual('VI', roman_number)
        
    def test_nine_to_roman(self):
        roman_number = self.roman_number.int_to_roman(9)
        self.assertEqual('IX', roman_number)

    def test_ten_to_roman(self):
        roman_number = self.roman_number.int_to_roman(10)
        self.assertEqual('X', roman_number)
    
    def test_forty_to_roman(self):
        roman_number = self.roman_number.int_to_roman(40)
        self.assertEqual('XL', roman_number)
    
    def test_fifty_to_roman(self):
        roman_number = self.roman_number.int_to_roman(50)
        self.assertEqual('L', roman_number)
    
    def test_ninety_to_roman(self):
        roman_number = self.roman_number.int_to_roman(90)
        self.assertEqual('XC', roman_number)

    def test_hundred_to_roman(self):
        roman_number = self.roman_number.int_to_roman(100)
        self.assertEqual('C', roman_number)

    def test_four_hundred_to_roman(self):
        roman_number = self.roman_number.int_to_roman(400)
        self.assertEqual('CD', roman_number)

    def test_five_hundred_to_roman(self):
        roman_number = self.roman_number.int_to_roman(500)
        self.assertEqual('D', roman_number)

    def test_nine_hundred_to_roman(self):
        roman_number = self.roman_number.int_to_roman(900)
        self.assertEqual('CM', roman_number)    

    def test_thouthand_to_roman(self):
        roman_number = self.roman_number.int_to_roman(1000)
        self.assertEqual('M', roman_number)

if __name__ == "__main__":
    unittest.main()