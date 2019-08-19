target, nums_str = [i for i in input().split()]
target = int(target)
nums_str = nums_str[1:]
nums_str = nums_str[:-1]
nums = [int(n) for n in nums_str.split(',')]

res = 0

res_set = set()

def slove(target, current, current_set):
    global res
    if current > target:
        return
    elif current == target:
        current_set.sort()
        t = tuple(current_set)
        if t not in res_set:
            res_set.add(t)
            res = res + 1
        return
    for idx,n in enumerate(nums):
        next_set = list(current_set)
        next_set.append(idx)
        slove(target=target, current=current + n, current_set=list(next_set))

slove(target,0, list())
print(res)