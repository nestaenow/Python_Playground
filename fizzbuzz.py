for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
        continue
    elif number % 5 == 0:
        print('Buzz')
        continue
    elif number % 3 == 0:
        print('Fizz')
        continue
    print(number)
