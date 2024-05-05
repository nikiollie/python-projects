
def ret_elements(listVar, evenOrOdd):
    if evenOrOdd == "even":
        return listVar[::2]
    elif evenOrOdd == "odd":
        return listVar[1::2]
    else:
        return "Not a valid option, can only be even or odd"
    


if __name__ == "__main__":
    listVar = ["apple", "banana", "grape", "cherry", "orange", "watermelon"]
    print(ret_elements(listVar, "odd"))
