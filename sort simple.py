def Interchange(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr1=[2,8,1,9,4,5]
print("kết quả sau khi sắp xếp tăng dần",Interchange(arr1))

def Interchange(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
print("kết quả sau khi sắp xếp giảm  dần",Interchange(arr1))
