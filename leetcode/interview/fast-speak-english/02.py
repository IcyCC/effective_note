
timer = {}
for i in range(0,2400):
    timer[i] = 0

starts = input().split()
ends = input().split()

for i in range(len(starts)):
    for t in range(int(starts[i]), int(ends[i])):
        timer[t] = timer[t] + 1

print(max(timer.values()))