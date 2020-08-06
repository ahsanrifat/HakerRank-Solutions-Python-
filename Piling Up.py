# test_case=1
test_case=int(input())
for _ in range(test_case):
    batil=input()
    arr=str(input())
    # arr="1 2 5 3 4 6 8 2 10"
    done=False
    arr=list(map(int,arr.split(" ")))
    sort=dict((k,2) for k in arr)
    sort=dict(sorted(sort.items()))
    for i in range(len(arr)):
        
        if arr[0]>=arr[-1]:
            pick=arr[0]
            del arr[0]
        else:
            pick=arr[-1]
            del arr[-1]
        
        if pick in sort:
            del sort[pick]
        if(len(sort)==0):
            break
        big_val=list(sort.keys())[-1]
        
        if big_val>pick:
            done=True
            print("No")
            break
    if done==False:
        print("Yes")
       
    