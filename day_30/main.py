# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("X")
# except KeyError as error_message:
#     print(f"Thw key {error_message} doesnt exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldnt be over 3 meters")

bmi = weight / height ** 2
print(bmi)