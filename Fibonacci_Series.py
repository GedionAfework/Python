#THIS PYTHON FILE IS FOR THE FIBONACCI SERIES, I HAVE WRITTEN SOME FUNCTIONS FOR THE SERIES.
def fibonacci(num):
    lst = [0, 1]
    i = 2
    while i < num:
        a = lst[len(lst) - 1] + lst[len(lst) - 2]
        lst.append(a)
        i += 1
    b = 0
    while b < len(lst):
        print(lst[b])
        b += 1
def fib_int(first, second):
    lst = [0, 1]
    i = 2
    while i < second:
        a = lst[len(lst) - 1] + lst[len(lst) - 2]
        lst.append(a)
        i += 1
    pre = first - 1
    while pre < second:
        print(lst[pre])
        pre += 1
def fibo(nu):
    first = 0
    second = 1
    for i in range(2, nu):
        fib = first + second
        first = second
        second = fib
        i += 1
    print(fib)
def fib_sum(number):
    first = 0
    second = 1
    sum = 1
    for i in range(2,number):
        fib = first + second
        first = second
        second = fib
        sum += fib
        i += 1
    print(sum)
choice = input("a. List all fibonacci series"
               "\nb. give me the fibonacci number at this interval"
               "\nc. give me the fibonacci series at this index"
               "\nd. sum of all the fibonacci series until this number"
               "\nWhich fibonacci operation do you want to work on?: ")
if choice.upper() == "A":
    num = int(input("Enter the index you want the fibonacci series for: "))
    fibonacci(num)
elif choice.upper() == "B":
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    fib_int(first, second)
elif choice.upper() == "C":
    nu = int(input("Enter at which index you want the Fibonacci series of: "))
    fibo(nu)
elif choice.upper() == "D":
    number = int(input("Enter a number: "))
    fib_sum(number)
