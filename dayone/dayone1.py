import re

list=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def get_first_digit(line):
  result = re.search(r"\d", line)
  return result.group()[0]

def get_last_digit(line):
  result = re.search(r"\d", line[::-1])
  return result.group()[::-1]

def main():
  numbers = 0

  with open('input.txt', 'r') as input:
    line = input.readline()

    while line != '':
      first = get_first_digit(line)
      last = get_last_digit(line)

      number = int(first + last)
      numbers += number

      print(f'number: {number},  addition = {numbers}')

      line = input.readline()

  print(numbers)


if __name__ == '__main__':
  main()
