name = "ada loveLace"
print(name.title())
print(name.lower())
print(name.upper())


#fstrings

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)


#whitespace
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_langauge = 'python     '
favorite_langauge = favorite_langauge.strip()
print(favorite_langauge)