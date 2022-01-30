#3-1 Names
names = ['paul','john','stephan']
print(names[0], names[1], names[2])


#3-2 Greetings
message = f"Hello {names[0].title()}"
print(message)


#3-3 Your Own List
transportation = ['motorcycle', 'car', 'bus']
message = f"I would like to own a {transportation[0]}"
print(message)


#3-4-3.7 Guest List

guest_list = ['paul', 'john', 'bob', 'alice' ]
print(guest_list)

message = f"{guest_list[-1].title()} cannot make it"
print(message)
del guest_list[-1]
print(guest_list)


guest_list.insert(0, 'darth')
guest_list.insert(2, 'dill')
guest_list.append('kyle')

print(guest_list)


print("I can only invite two people.")

for guest in guest_list[2:]:
    guest_list.remove(guest)
    print(f"Sorry, {guest}")

for guest in guest_list:
    print(f"{guest} is invited!")

del guest_list[1]
del guest_list[0]

print(guest_list)