
def maxvalue(arr, index):
    if index > 0:
        return arr[index] if arr[index] > maxvalue(arr, index - 1) else maxvalue(arr, index - 1)
    else:
        return arr[0]
  



arr = [7, 3, 1, 0, 4, 9, 2, 8, 5, 6]

maxvalue(arr, len(arr) - 1)


