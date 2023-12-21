# list = [5, 15, 9, 1, 3, 19, 7, 8, 2]
# Greatest_digits = 0
smallest_digits = 1
for num in list:
    if num > Greatest_digits:
        Greatest_digits = num
print(Greatest_digits)
for num in list:
    if num < smallest_digits:
        smallest_digits = num
print(smallest_digits)
User_input = input("enter your input: ")
User_input = " greeksforgreeks "
string = " "
for i in User_input:
    # print(i)
    if User_input.count(i) == 1:
        string += i
        print(string)
        break

