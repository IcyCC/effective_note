def lower_bound(arrary, fist, last, value):
    while fist < last:
        mid = fist + (last- fist) // 2
        if arrary[mid] < value:
            fist = mid + 1
        else:
            last = mid
    return fist