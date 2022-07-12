def fizz_buzz(num):
    iteration = range(num + 1)
    for n in iteration:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)


fizz_buzz(100)
fizz_buzz(50)
