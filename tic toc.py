inp_field_size = int(input("Please enter filed size, 1 numbers >>"))

numbers_by_coordinates = [["" for _ in range(inp_field_size)]for i in range(inp_field_size)]


# Счетчики
count = 0


#print(len_numbers_by_coordinates)

#print('Please user 1 choose your symbol X or 0')

symbol_for_user1 = input('Please user 1 choose your symbol X or 0 >>')
symbol_for_user2 = input('Please user 2 choose your symbol X or 0 ??')

print()

while count < inp_field_size * inp_field_size:

    print("Please, enter 2 numbers(coordinates x, y) and symbol(X or 0) with space, press enter >>")

    try:
        user_1 = input("user_1 enter x, y: ").split()
        user_2 = input("user_2 enter x, y: ").split()
        convert_int_user1 = (int(user_1[0]), int(user_1[1]))
        convert_int_user2 = (int(user_2[0]), int(user_2[1]))

        if numbers_by_coordinates[convert_int_user1[0]][convert_int_user1[1]] == "":
            numbers_by_coordinates[convert_int_user1[0]][convert_int_user1[1]] = symbol_for_user1
            count += 1
            #print(numbers_by_coordinates)
        else:
            print(f"Try again another coordinates user 1. The coordinates "
                  f"x: {convert_int_user1[0]} and y:{convert_int_user1[1]} coordinates you entered were used earlier")
    except IndexError:
        print("Please user 1, try another index x: 0-2 and y: 0-2 ")
        continue

    try:
        if numbers_by_coordinates[convert_int_user2[0]][convert_int_user2[1]] == "":
            numbers_by_coordinates[convert_int_user2[0]][convert_int_user2[1]] = symbol_for_user2
            flag = user_2
            count += 1
            #print(numbers_by_coordinates)
        else:
            print(f"Try again another coordinates user 2. The coordinates "
                  f"x: {convert_int_user2[0]} and y:{convert_int_user2[1]} coordinates you entered were used earlier")
    except IndexError:
        print("Please user 2, try another index x: 0-2 and y: 0-2 ")
        continue

    print(count)
    print(numbers_by_coordinates)



diagonal_element_count, counting_elements_by_vertical = 0, 0
list_vertical_numbers = []
winner = ""

# по Диагонали
for diagonal_line in range(len(numbers_by_coordinates)):
    for column_diagonally in range(len(numbers_by_coordinates)):
        if diagonal_line == column_diagonally:
            if numbers_by_coordinates[diagonal_line][column_diagonally] == symbol_for_user1:
                diagonal_element_count += 1
                winner = "по Диагонали user 1"
                print(numbers_by_coordinates[diagonal_line][column_diagonally])

            elif numbers_by_coordinates[diagonal_line][column_diagonally] == symbol_for_user2:
                diagonal_element_count += 1
                winner = "по Диагонали User 2"
                print(numbers_by_coordinates[diagonal_line][column_diagonally])
                # print(diagonal_element_count)
            else:
                diagonal_element_count = 0



# по вертикали
for vertical_column in range(len(numbers_by_coordinates)):
    for vertical_line in range(len(numbers_by_coordinates)):
        list_vertical_numbers.append((vertical_column, numbers_by_coordinates[vertical_line][vertical_column]))

for index_and_numbers in list_vertical_numbers:
    if list_vertical_numbers.count(index_and_numbers) == 3 and index_and_numbers[1] == symbol_for_user1:
        winner = "по Вертикали user 1"
        break
    elif list_vertical_numbers.count(index_and_numbers) == 3 and index_and_numbers[1] == symbol_for_user2:
        winner = "по Вертикали User 2"
        break

# ПО горизонтали
for row in numbers_by_coordinates:
    if row.count(symbol_for_user1) == 3:
        winner = "по Горизонтали user 1"
        break
    elif row.count(symbol_for_user1) == 3:
        winner = "по Горизонтали user 2"
        break

print(winner)

'''if diagonal_element_count == 3:
                   print(winner)'''