def first_occur(arr):
    num=set()
    for i in range(len(arr)):
        if arr[i] in num:
            return arr[i]
        else:
            num.add(arr[i])
            
print(first_occur([1,2,3,2,1]))

        
