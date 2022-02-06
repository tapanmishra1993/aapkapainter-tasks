def score_count(arr):
    p1=0
    p2=0
    score=0
    for i in range(len(arr)):
        if score%2==0:
            p1+=+arr[i]
            score+=arr[i]
        else:
            p2=p2+arr[i]
            score+=arr[i]    
    print("p1 : ",p1,", p2 :",p2)
score_count([1,2,3,1,2])