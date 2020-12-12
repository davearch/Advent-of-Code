with open('input2.txt') as f:
    data = f.readlines()

policies = {}
for idx, line in enumerate(data):
    if (line[-1] == '\n'):
        data[idx] = line[:-1]
    else:
        data[idx] = line

# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at
# least 1 time and at most 3 times.

# O(n)
for line in data:
    key, value = line.split(':')
    if key in policies:
        policies[key].append(value.strip())
        continue
    policies[key] = [value.strip()]

count = 0
# O(n^2) for each string we count each letter
for k, v in policies.items():
    _min = int(k.split('-')[0])
    _max = int(k.split('-')[1][:-2])
    letter = k.split(' ')[1]
    # still O(n) because I'm counting by the rows
    # not by each list item :)~
    for itm in v:
        # O(n) for counting by each letter
        l_count = itm.count(letter)
        if l_count >= _min and l_count <= _max:
            count += 1

# O(n)
sec_count = 0
for k, v in policies.items():
    _min = int(k.split('-')[0])
    _max = int(k.split('-')[1][:-2])
    letter = k.split(' ')[1]
    for itm in v:
        if (itm[_min-1] == letter) ^ (itm[_max-1] == letter):
            sec_count += 1
print(sec_count)
