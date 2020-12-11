# Find the two entries that sum to 2020;
# what do you get if you multiply them together?
with open('input.txt') as f:
    data = f.readlines()

for idx, line in enumerate(data):
    if (line[-1] == '\n'):
        data[idx] = line[:-1]
    data[idx] = int(line)

# O(n) runtime
target = 2020
seen = set()
for line in data:
    diff = target - line
    if diff in seen:
        print(diff * line)
    seen.add(line)


# part two
# what is the product of the three entries that sum to 2020?
target = 2020
# O(nlog(n))
data.sort()
# O(n^2) o_O
for i in range(len(data)):
    lo = i + 1
    hi = len(data) - 1
    while (lo < hi):
        mid = (lo + hi) // 2
        _sum = data[lo] + data[hi] + data[i]
        if _sum > target:
            hi -= 1
        elif _sum < target:
            lo += 1
        else:
            print(data[i] * data[lo] * data[hi])
            break
