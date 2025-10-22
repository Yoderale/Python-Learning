"""2-7. Stripping Names: Use a variable to represent a person’s name, and
include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()."""

first_name = " kylie  "
last_name = "yOder "

print(f'{first_name} {last_name}')
print(first_name.lstrip())
print(last_name.rstrip())
print(first_name.strip())


first_name_stripped = first_name.strip().title()  
last_name_stripped = last_name.strip().title()
name_stripped = first_name_stripped + ' ' + last_name_stripped
print(f'{name_stripped}')
