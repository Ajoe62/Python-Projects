import random 

name = input("Please enter a name: ")
print(f"Hello {name}, welcome to the password generator.")

pass_len = int(input("Enter the length of the password: "))
pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"

password = "".join(random.sample(pass_data, pass_len))

print(password)