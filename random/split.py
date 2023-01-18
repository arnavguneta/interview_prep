def calc(input):
  hmap = {}
  (nums, eq) = input.split(' ')
  print(nums, eq)
  eq_i = 0
  op = ''
  for i in range(0, len(nums)):
    if eq[eq_i] == '+' or eq[eq_i] == '-':
      op = eq[eq_i]
      eq_i += 1
    hmap[f"{op}{eq[eq_i]}"] = nums[i]
    eq_i += 1
  print(hmap)
  nums = ['', '']
  nums_i = 0
  for key in hmap:
    if op in key:
      nums_i = 1
    nums[nums_i] += hmap[key]
  print(nums)
  return int(nums[0]) + int(nums[1])  if op is '+' else int(nums[0]) - int(nums[1]) 

print(calc('12345 ba-cde'))