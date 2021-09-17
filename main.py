class RomanNumeralsHelper:
  def __init__(self):
    self.numerals = {
        '2000': 'MM', '1000': 'M', '0000': '', '900': 'CM', '800': 'CCM',
        '700': 'DCC', '600': 'DC', '500': 'D', '400': 'CD', '300': 'CCD',
        '200': 'CC', '100': 'C', '000': '', '90': 'XC', '80': 'XXC',
        '70': 'LXX', '60': 'LX', '50': 'L', '40': 'XL', '30': 'XXL',
        '20': 'XX', '10': 'X', '00': '', '9': 'IX', '8': 'IIX',
        '7': 'VII', '6': 'VI', '5': 'V', '4': 'IV', '3': 'IIV',
        '2': 'II', '1': 'I', '0': ''
    }

  def to_roman(self, number):
    roman_numeral = ''
    for i in range(len(str(number))):
      roman_numeral += self.numerals[str(number)[i] + ('0' * (len(str(number)) - (i + 1)))]
    return roman_numeral

  def convert_single_numeral_value(self, numeral):
    for value in self.numerals.values():
      if value == numeral:
        index = list(self.numerals.values()).index(value)
        key = list(self.numerals.keys())[index]
        return int(key)

  def split_numeral(self, numeral):
    length = len(numeral)
    if length == 0:
      return 0
    if length == 1:
      return [numeral]
    starting_chars = ['D', 'C', 'L', 'X', 'V', 'I']
    partners = {'D': 'C', 'C': 'D', 'L': 'X', 'X': 'L', 'V': 'I', 'I': 'V'}
    ind = ''
    numerals = []
    if numeral[0] not in starting_chars:
      if numeral[1] not in starting_chars:
        numerals.append(numeral[0:2])
        numeral = numeral[2:]
      else:
        numerals.append(numeral[0])
      numeral = numeral[1:]
    for char in numeral:
      if char in starting_chars:
        if char == 'I' or char == 'V':
          starting_chars.clear()
        elif starting_chars.index(char) > starting_chars.index(partners[char]):
          starting_chars = starting_chars[starting_chars.index(char) + 1:]
        else:
          starting_chars = starting_chars[starting_chars.index(partners[char]) + 1:]
        numerals.append(ind)
        ind = ''
      ind += char
    numerals.append(ind)
    numerals.remove('')
    return numerals

  def from_roman(self, numeral):
    number = 0
    numeral_list = self.split_numeral(numeral)
    for numeral in numeral_list:
      number += self.convert_single_numeral_value(numeral)
    return number


calc = RomanNumeralsHelper()

for i in range(1, 101):
  roman = calc.to_roman(i)
  number = calc.from_roman(roman)
  print(f'{i} : {roman} : {number}')
  