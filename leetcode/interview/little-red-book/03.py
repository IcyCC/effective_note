# from functools import lru_cache
# num = int(input())
# notes = [int(i) for i in input().split()]
#
# _max_res = 0
# _min_pick = 0
#
# @lru_cache(10000)
# def slove(current_idx, current_res, current_pick):
#     global _max_res
#     global _min_pick
#     if current_idx >= len(notes):
#         return
#
#     current_res = current_res + notes[current_idx]
#     current_pick = current_pick + 1
#
#     if current_res > _max_res:
#         _max_res = current_res
#         _min_pick = current_pick
#     elif current_res == _max_res:
#         _min_pick = min(_min_pick, current_pick)
#
#     for next_idx in range(current_idx + 2, len(notes)):
#         slove(next_idx, current_res, current_pick)
#
#
#
# for i in range(0, len(notes)):
#     slove(i, 0, 0)
#
# print("{} {}".format(_max_res, _min_pick))
#
#
#


num = int(input())
notes = [int(i) for i in input().split()]

f = [(0,0) for i in range(len(notes) + 1)]
pick = 0
f[1] = (notes[0], 1)
for i in range(2, len(notes)+1):
    idx = i - 1
    v = notes[idx]
    if f[i-2][0]+ v > f[i-1][0]:
        # 选取
        f[i] = (f[i-2][0] + v, f[i-2][1] + 1)
    else:
        f[i] = (f[i-1][0] + 0, f[i-1][1] +0)

print("{} {}".format(f[len(notes)][0], f[len(notes)][1]))





