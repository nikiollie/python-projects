def palindrome(string):
    #basic way
    #for i, char in enumerate(string):
    #    if char != string[len(string)-i-1]:
    #        return False
    #return True

    #optimized way using slicing
    if string[::1] == string[::-1]:
        return True
    else:
        return False

#two pointer method
def two_pointer_palindrome(string):
    a, b = 0, len(string)-1
    while a < b:
        while a < b and not string[a].isalnum():
            a += 1
        while b > a and not string[b].isalnum():
            b-=1
        if string[a].lower() != string[b].lower():
            return False
        a+=1
        b-=1 

    return True


print(two_pointer_palindrome("toppot"))
print(two_pointer_palindrome("cat"))
