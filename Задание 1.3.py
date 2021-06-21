def div(number1, number2):
  try:
  number1, number2 = int(number1), int(number2)
  number = number1/ number2
  except ValueError:
  return 'ValueError'
  except ZeroDivisionError:
  return 'ZeroDivisionError'
  return round(number, 4)
print(div(input('Введите первое число  '), input('Введите второе число  ')))

