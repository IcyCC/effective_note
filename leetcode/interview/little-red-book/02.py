res = input().split()

def reverseString(s) -> None:
    if not s or len(s) == 1:
        return
    l = 0
    h = len(s) - 1
    while l < h:
        s[l], s[h] = s[h], s[l]
        l = l + 1
        h = h - 1

if res:
    reverseString(res)
print(' '.join(res))