
# 5 * 4 * 3 * 2 * 1
def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i

    print(res)

#return number of trailing zeroes for factorial of a num
def trailingZeroes(num):
    count = 0
    while num>=5:
        num //=5
        count += num
    print(count)

trailingZeroes(int(input("Input a number: ")))
