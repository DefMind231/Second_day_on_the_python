password = " "
attempts = 0

while password != "google750k":
	password = input("Enter the code: ")
	attempts = attempts + 1
	if password != "google750k":
		print("Access is danied!")

print("Access is open!")
print("It took you this many tries:")
print(attempts)
