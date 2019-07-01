# bubble, insertion, selection -> insertion이 나음

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j=i-1
        while j!=-1:
            if arr[j] > temp:
                arr[j+1]=arr[j]
                j-=1
            else:
                break
        arr[j+1]=temp

if __name__ == "__main__":
    arr = [2, 5, 1, 3, 12, 8]
    insertion_sort(arr)
    print(arr)