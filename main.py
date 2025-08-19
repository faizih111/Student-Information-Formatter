name = input("Enter your name: ")
course = input("Enter your course: ")
quote = input("Enter your favorite quote: ")

print("___Student Information Formatter___")

print("Name:", name)
print("Initial:", name[:1] + "." + name[10:])
print("Course:", f"{course} (Leangth: {len(course)})")

Quote = quote.replace("Weaknes", "Power")
print("Favorite Quote:", Quote)
print("Reversed Name:", name[::-1])
