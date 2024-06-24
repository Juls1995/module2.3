my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for number in my_list:
    if number >= 1:
        print(number)
    if number == 0:
        continue
    if number <= -1:
        break