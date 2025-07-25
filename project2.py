name = input("enter your name :- ")

age = input("enter your age :- ")

height = input("enter your height in meters :- ")

favnum = name = input("enter your favourite number :-")

age = int(age)

print("Converted datatype of age from str to int")


height = float(height)

print("Converted datatype of height from str to float")

favnum = int(favnum)

print("Converted datatype of age from str to int")

print(f"Data type of name :- {type(name)}")
print(f"Data type of age :- {type(age)}")
print(f"Data type of height :- {type(height)}")
print(f"Data type of favourite number :- {type(favnum)}")

print(f"Your Birth Year :- {2025 - age}")

print(f"Memory Address of name :- {id(name)}")
print(f"Memory Address of age :- {id(age)}")
print(f"Memory Address of height :- {id(height)}")
print(f"Memory Address of favourite number :- {id(favnum)}")