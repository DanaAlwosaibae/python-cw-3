# write your code here
favorit_animals=['cat','dog','monkey','rabbit']
print(favorit_animals)
print(favorit_animals.pop(1)) 
favorit_animals.remove('monkey')
favorit_animals.append('ant')
for animal in favorit_animals:
    print(f'i love {animal}')
numbers=[1,2,3,4,5]
numbers_sum=0
for num in numbers:
    numbers_sum+=num
print(numbers_sum)