def Insertion(arr):
    n = len(arr)
    for i in range(1, n):
        tam = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < tam:# Dịch chuyển các phần tử nhỏ hơn key sang phải để chèn key vào đúng vị trí giảm dần
            arr[j + 1] = arr[j]
            j -= 1#giảm j
        arr[j + 1] = tam
    return arr
arr1 = [5, 2, 9, 1, 5, 6]
print("kết quả sau khi sắp xếp giảm dần", Insertion(arr1))

def Insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key sang phải để chèn key vào đúng vị trí tăng dần
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print("kết quả sau khi sắp xếp tăng dần", Insertion(arr1))