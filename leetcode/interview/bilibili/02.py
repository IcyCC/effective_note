nums = input().split(',')

def mycmp(a,b):
    l = min(len(a), len(b))
    i = 0
    for i in range(l):
        if int(a[i]) < int(b[i]):
            return True
        elif int(a[i]) > int(b[i]):
            return False
    if l < len(a):
        return a[i+1] < a[i]
    elif l < len(b):
        return b[i+1] > b[i]
    else:
        return True

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if not mycmp(nums[i], nums[j]):
            nums[i],  nums[j] =  nums[j], nums[i]


print(''.join(nums))

