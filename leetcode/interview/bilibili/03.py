s = input().split()
start = 0
end = len(s) - 1

while start < end:
    s[start], s[end] = s[end], s[start]
    start = start + 1
    end = end - 1

print(" ".join(s))
