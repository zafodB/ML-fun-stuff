'''
 * Created by filip on 26/02/2019
'''


def ___init___():

    def is_valid_piece(start_tile_row, start_tile_column, direction_right, distance):
        count_tomatoes = 0
        count_mushrooms = 0

        if direction_right:
            for i in range(0, distance):
                if start_tile_column + i >= len(pizza[0]):
                    break
                if pizza[start_tile_row][start_tile_column + i][0] == 'T':
                    count_tomatoes += 1
                else:
                    count_mushrooms += 1
        else:
            for i in range(0, distance):
                if start_tile_row + i >= len(pizza):
                    break
                if pizza[start_tile_row + i][start_tile_column][0] == 'T':
                    count_tomatoes += 1
                else:
                    count_mushrooms += 1

        if count_mushrooms >= min_ingredient and count_tomatoes >= min_ingredient:
            print("This IS a valid piece")
            return True
        else:
            print("This is NOT a valid piece")
            return False


    f = open("a_example.in", "r")

    first_line_numbers = f.readline().split()

    rows = int(first_line_numbers[0])
    columns = int(first_line_numbers[1])
    min_ingredient = int(first_line_numbers[2])
    max_slice_size = int(first_line_numbers[3])

    # arr = []
    # arr = first_line.split()

    pizza = []

    i = 0
    for line in f:

        pizza.append([])

        for letter in line:
            if letter != "\n": pizza[i].append([letter, 0])

        print(pizza[i])
        i += 1

    # print(pizza)
    # print(type(rows))
    for row in range(0, rows):
        # print(pizza[row])
        for column in range(0, columns):
            # print(pizza[row][column])
            if pizza[row][column][1] == 0:
                found_piece = False

                for l in range(1, max_slice_size + 1):
                    found_piece = is_valid_piece(start_tile_row = row, start_tile_column=column, direction_right=False,
                                   distance=l)
                    if found_piece:
                        break
                for l in range(1, max_slice_size + 1):
                    found_piece = is_valid_piece(start_tile_row = row, start_tile_column=column, direction_right=True,
                                   distance=l)
                    if found_piece:
                        break




                # print("TOMATOOO")




___init___()
