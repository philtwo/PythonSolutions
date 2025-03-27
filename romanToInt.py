def romanToInt(s: str) -> int:
    """
    Convert a Roman numeral to an integer.
    
    :param s: A string representing a Roman numeral.
    :return: The integer value of the Roman numeral.
    """
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number = 0
    # Replace subtractive combinations with their additive equivalents
    s.replace("IV", "IIII"), s.replace("IX", "VIIII"), s.replace("XL", "XXXX"), s.replace("XC", "LXXXX"), s.replace("CD", "CCCC"), s.replace("CM", "DCCCC")
    for char in s:
        number += roman_to_int[char]
    return number

print(romanToInt("III")) # 3 
print(romanToInt("IV")) # 4 
print(romanToInt("IX")) # 9 
print(romanToInt("LVIII")) # 58 