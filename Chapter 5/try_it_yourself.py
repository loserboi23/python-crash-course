#5-1 Conditional Tests

car = 'sabaru'
print("Is car == 'sabaru'? I predict True.")
print(car == 'sabaru')


print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5-2 More Conditonal Tests

car = 'sabaru'
type = 'Sabaru'
print(car == type.lower())

print(1 == 1)

print((1==1) and (3==2))

print((1==1) or (1==2))

banned_users = ['andrew', 'carolina', 'david']

print('andrew' in banned_users)
print('carolina' not in banned_users)

#5-3 - 5.5 Alien Colors

alien_color = ['green','red','yellow']

color = 'green'

if color == 'green':
    print("earned 5 points")
elif color == 'yellow':
    print("earned 10 points")
elif color == 'red':
    print('earned 15 points')

#5-6 stages of life

age = 0

if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("elder")