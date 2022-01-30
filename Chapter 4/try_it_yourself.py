
# 4-1 Pizzas

pizza_type = ['cheese', 'pepperoni', 'pineapple']
for type in pizza_type:
    print(f"I like {type} pizza.")

# 4-2 Animals

animal_type = ["dog", "cat", "cow"]

for type in animal_type:
    print(f"A {type} would make a great pet!")
print("Any of these animals would make a great pet")

#4-3
for r in range(0,21):
    print(r)

#4-4 One Million
numbers = list(range(1,1_000))
for number in numbers:
    print(number)   

#4-5 Summing a million

min = min(numbers)
max = max(numbers)
sum = sum(numbers)

print(min, max, sum)


#4-6 Odd Numbers
numbers = list(range(1,20,3))
print(numbers)


#4-7 Threes 
numbers = list(range(3, 31, 3))
for n in numbers:
    print(n)

#4-8 Cubes & Cubes Comprehension 
list = []
for r in range(1,11):
    list.append(r**3)

print(list)
del list
list = [r**3 for r in range(1,11)]
print(list)

    