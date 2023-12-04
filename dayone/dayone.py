import re

num_list=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def change_to_string_of_int(word_list, word):
  return str(word_list.index(word) + 1)


def get_first_digit(line):
  results_word = re.compile('|'.join(num_list), re.IGNORECASE).findall(line)
  result_digits = re.findall(r'\d', line)
  print(f'first digit results: {result_digits}')
  print(f'last word results: {results_word}')


  if len(results_word) > 0:
    word_postion = line.find(results_word[0])
    digit_position = line.find(result_digits[0]) if len(result_digits) > 0 else 100000

    print(f'last digit position: {digit_position}')
    print(f'last word position: {word_postion}')

    if len(result_digits) == 0 or word_postion < digit_position:
      return change_to_string_of_int(num_list, results_word[0])
    else:
      return result_digits[0]
  else:
    return result_digits[0]

def get_last_digit(line):

  results_word = re.compile('|'.join(num_list), re.IGNORECASE).findall(line)
  result_digits = re.findall(r'\d', line)
  print(f'last digit results: {result_digits}')
  print(f'last word results: {results_word}')


  if len(results_word) > 0:
    word_postion = line.rfind(results_word[-1])
    digit_position = line.rfind(result_digits[-1]) if len(result_digits) > 0 else 0

    print(f'last digit position: {digit_position}')
    print(f'last word position: {word_postion}')

    if len(result_digits) == 0 or word_postion > digit_position:
      return change_to_string_of_int(num_list, results_word[-1])
    else:
      # print(f'return digit: {result_digits[-1]}')
      return result_digits[-1]
  else:
    return result_digits[-1]


def main():
  numbers = 0

  with open('input.txt', 'r') as input:
    print('\n\n')
    line = input.readline()

    while line != '':
      print(f'{line}')
      first = get_first_digit(line)
      last = get_last_digit(line)

      number = int(first + last)
      numbers += number
      print(f'number: {number},  addition = {numbers}\n\n')

      line = input.readline()

  print(numbers)


if __name__ == '__main__':
  main()
