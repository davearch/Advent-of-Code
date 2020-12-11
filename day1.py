# Find the two entries that sum to 2020;
# what do you get if you multiply them together?
expenses = []
with open('input.txt') as f:
    data = f.readlines()

for idx, line in enumerate(data):
    if (line[-1] == '\n'):
        data[idx] = line[:-1]
    data[idx] = int(line)

# O(n) runtime
target = 2020
seen = set()
for idx, line in enumerate(data):
    diff = target - line
    if diff in seen:
        print(diff * line)
    seen.add(line)
