
def return_largest(listVar):
    largest = 0
    for num in listVar:
        if num > largest:
            largest = num

    #return max(listVar)
    return largest


if __name__ == "__main__":
    print(return_largest([5,1,3,8,6,5]))
    print(return_largest([6,9,10,22,1]))
