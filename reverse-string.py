def reverse(var):
    for i in range(len(var)):
        print(var[len(var)-i-1], end="")

    print("\n")

    #print(var[::-1])

if __name__ == "__main__":
    reverse_string = input("Input a string to reverse: ")
    reverse(reverse_string)
