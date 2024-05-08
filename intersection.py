def intersection(arr1, arr2):
    num_list = []
    result = []
    for i in arr1:
        if i in num_list:
            continue
        else:
            num_list.append(i)

    for i in arr2:
        if i in num_list and i not in result:
            result.append(i)
    return result
    
#sort arrays and use 2 pointers        
#def intersection_2_ptr(arr1, arr2):
    

print(intersection([1,3,6,6,7], [3,7,7,9])) #[3, 7]
print(intersection([8,3,2,5,5,9,1], [3,9,1,4,4,2])) #[3, 2, 9, 1]
print(intersection([3,3], [1])) #[]
