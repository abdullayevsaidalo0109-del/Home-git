def majority_element(numbers: list) ->int:
    dct ={}
    for i in numbers:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] +=1
    return max(dct, key=dct.get)
        
numbers =  [2, 2, 1, 1, 1, 2, 2]
print(majority_element(numbers))