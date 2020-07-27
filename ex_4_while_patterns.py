n = 0

while n < 9:
    n += 1
    #if n == 1 or n == 4 or n == 7:
    if n % 3 == 1:
        print(n, "*")
    else:
        print(n, "#")