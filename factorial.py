# This function is used to get the factorial of its input value
def factorial(n):
    if (n == 0):
        return 1
    else:
        return factorial(n-1) * n
