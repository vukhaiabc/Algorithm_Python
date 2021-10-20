class Test:
    def convert_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
            ]
        sign = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_sign = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_sign += sign[i]
                num -= val[i]
            i += 1
        return roman_sign

test = Test()
print(test.convert_to_Roman(9))
print(test.convert_to_Roman(1994))