input = '1 -1 2 3 -5'
nums = []

for i in input.split(' '):
    nums.append(int(i))

print(str(min(nums)) + ' ' + str(max(nums)))