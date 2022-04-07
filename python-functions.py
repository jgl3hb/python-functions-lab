def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

sum_to(6)
print(sum_to(6))

sum_to(10)
print(sum_to(10))

def largest(nums):
  largest = 0 
  for num in nums: 
    if num > largest: 
      largest = num
  return largest

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

def occurrences(string, occ):
  return string.count(occ)

print(occurrences('fleep floop', 'e') )  # returns 2
print(occurrences('fleep floop', 'p'))  # returns 2
print(occurrences('fleep floop', 'ee'))  # returns 1
print(occurrences('fleep floop', 'fe'))  # returns 0

def product(*args):
  product = 1
  for arg in args: 
    product *= arg
  return product

print(product(-1, 4))  #-4
print(product(2, 5, 5))  #50
print(product(4, 0.5, 5))  #10.0