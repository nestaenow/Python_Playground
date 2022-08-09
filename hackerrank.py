# Challenge II
n = int(input())
if 1 <= n <= 20:
    for index in list(range(n)):
        print(index ** 2)

# Challenge IV
def is_leap(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0):
      # Note that in your code the condition will be true if it is not..
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      # For some reason here you had False twice
      leap = True
  else:
      leap = False

  return leap


year = int(input())
print(is_leap(year))

# Challenge V
n = int(input())
string_of_numbers = ''
if 1 <= n <= 150:
    for i in range(1, n+1):
        string_of_numbers += str(i)
    print(string_of_numbers)
else:
    print('Number not in range!!')

# A shorter solution
# list(map(lambda i: print(i, end=''), [i for i in range(1, int(input()) + 1)]))
