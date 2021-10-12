def shellsort(arr):
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):
    
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            
            i += 1
            j += 1
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1

        gap //= 2