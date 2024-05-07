
#0, 1, 1, 2, 3, 5, 8, 13, 21, etc

#using while loop and print
def generate_fibonacci():
    first_num = 0
    sec_num = 1
    print(first_num)
    print(sec_num)
    while sec_num < 200:
        first_num = first_num + sec_num
        print(first_num)
        sec_num = first_num + sec_num
        print(sec_num)

#using while loop with specified limit and yield
def fib_generator(limit):
    first_num = 0
    sec_num = 1
    while first_num < limit:
        yield first_num
        first_num, sec_num = sec_num, first_num + sec_num


for i in fib_generator(5):
    print(i)
