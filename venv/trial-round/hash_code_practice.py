'''
 * Created by filip on 26/02/2019
'''


def ___init___():
    # f = open("a_example.in", "r")
    # f = open("b_small.in", "r")
    # f = open("c_medium.in", "r")
    f = open("d_big.in", "r")

    # f = open("a_example2.in", "r")

    first_line_numbers = f.readline().split()
    # print(first_line_numbers)

    rows = int(first_line_numbers[0])
    columns = int(first_line_numbers[1])
    min_ingredient = int(first_line_numbers[2])
    max_slice_size = int(first_line_numbers[3])

    slice_counter = 51

    pizza = []

    i = 0
    for line in f:

        pizza.append([])

        for letter in line:
            if letter != "\n": pizza[i].append([letter, 0, False])

        # print(pizza[i])
        i += 1

    def is_valid_piece(start_tile_row, start_tile_column, direction_right, distance):
        count_tomatoes = 0
        count_mushrooms = 0

        if direction_right:
            for i in range(0, distance):
                if start_tile_column + i >= len(pizza[0]):
                    break
                if pizza[start_tile_row][start_tile_column + i][1] != 0:
                    break
                if pizza[start_tile_row][start_tile_column + i][0] == 'T':
                    count_tomatoes += 1
                else:
                    count_mushrooms += 1
        else:
            for i in range(0, distance):
                if start_tile_row + i >= len(pizza):
                    break
                if pizza[start_tile_row + i][start_tile_column][1] != 0:
                    break
                if pizza[start_tile_row + i][start_tile_column][0] == 'T':
                    count_tomatoes += 1
                else:
                    count_mushrooms += 1

        if count_mushrooms >= min_ingredient and count_tomatoes >= min_ingredient:
            return True
        else:
            return False

    def mark_piece(start_tile_row, start_tile_column, direction_right, length):
        nonlocal slice_counter

        if direction_right:
            for i in range(0, length):
                pizza[start_tile_row][start_tile_column + i][1] = slice_counter
        else:
            for i in range(0, length):
                pizza[start_tile_row + i][start_tile_column][1] = slice_counter

        slice_counter += 1

    def find_smallest_pieces():
        for row in range(0, rows):
            for column in range(0, columns):
                if pizza[row][column][1] == 0:
                    found_piece = False

                    for l in range(1, max_slice_size + 1):
                        found_piece = is_valid_piece(row, column, False, l)
                        if found_piece:
                            mark_piece(row, column, False, l)
                            break

                    if found_piece:
                        continue

                    for l in range(1, max_slice_size + 1):
                        found_piece = is_valid_piece(row, column, True, l)
                        if found_piece:
                            mark_piece(row, column, True, l)
                            break

    def find_bounds_of_slice(start_tile_row, start_tile_column, slice_id):
        bound_right = 0
        bound_bottom = 0

        for i in range(0, max_slice_size + 1):
            if start_tile_row + i >= rows:
                bound_bottom = rows - 1
                break
            if pizza[start_tile_row + i][start_tile_column][1] != slice_id:
                bound_bottom = start_tile_row + i - 1
                break

        for j in range(0, max_slice_size + 1):
            if start_tile_column + j >= columns:
                bound_right = columns - 1
                break
            if pizza[start_tile_row][start_tile_column + j][1] != slice_id:
                bound_right = start_tile_column + j - 1
                break

        return [bound_bottom, bound_right]

    def calculate_slice_area(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right):
        return (slice_bound_right + 1 - start_tile_column) * (slice_bound_bottom + 1 - start_tile_row)

    def explore_to_the_top(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right, slice_id):
        expandable_row_number = -1
        for i in range(start_tile_row - 1, -1, -1):
            row_expandable = True

            for j in range(start_tile_column, slice_bound_right + 1):
                if pizza[i][j][1] != 0:
                    row_expandable = False
                    break

            if not row_expandable: break

            if calculate_slice_area(i, start_tile_column, slice_bound_bottom, slice_bound_right) > max_slice_size:
                row_expandable = False
                break

            expandable_row_number = i

        if expandable_row_number == - 1:
            return False
        else:
            return expandable_row_number

    def explore_to_the_left(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right, slice_id):
        expandable_column_number = -1

        for i in range(start_tile_column - 1, -1, -1):
            column_expandable = True

            for j in range(start_tile_row, slice_bound_bottom + 1):
                if pizza[j][i][1] != 0:
                    column_expandable = False
                    break

            if not column_expandable: break

            if calculate_slice_area(start_tile_row, i, slice_bound_bottom, slice_bound_right) > max_slice_size:
                column_expandable = False
                break

            expandable_column_number = i

        if expandable_column_number == - 1:
            return False
        else:
            return expandable_column_number

    def explore_to_the_bottom(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right, slice_id):
        expandable_row_number = -1
        for i in range(slice_bound_bottom + 1, rows):
            row_expandable = True

            for j in range(start_tile_column, slice_bound_right + 1):
                if pizza[i][j][1] != 0:
                    row_expandable = False
                    break

            if not row_expandable: break

            if calculate_slice_area(start_tile_row, start_tile_column, i, slice_bound_right) > max_slice_size:
                row_expandable = False
                break

            expandable_row_number = i

        if expandable_row_number == - 1:
            return False
        else:
            return expandable_row_number

    def explore_to_the_right(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right, slice_id):
        expandable_column_number = -1
        for i in range(slice_bound_right + 1, columns):
            column_expandable = True
            for j in range(start_tile_row, slice_bound_bottom + 1):
                if pizza[j][i][1] != 0:
                    column_expandable = False
                    break

            if not column_expandable: break

            if calculate_slice_area(start_tile_row, start_tile_column, slice_bound_bottom, i) > max_slice_size:
                column_expandable = False
                break

            expandable_column_number = i

        if expandable_column_number == - 1:
            return False
        else:
            return expandable_column_number

    def expand_to_top(start_tile_row, start_tile_column, slice_id):
        bounds = find_bounds_of_slice(start_tile_row, start_tile_column, slice_id)

        slice_bound_bottom = bounds[0]
        slice_bound_right = bounds[1]

        if start_tile_row >= 1 and calculate_slice_area(start_tile_row, start_tile_column,
                                                        slice_bound_bottom, slice_bound_right) < max_slice_size:

            expandable_row_top = explore_to_the_top(start_tile_row, start_tile_column,
                                                    slice_bound_bottom, slice_bound_right, slice_id)

            if type(expandable_row_top) == int:
                for i in range(expandable_row_top, start_tile_row + 1):
                    for j in range(start_tile_column, slice_bound_right + 1):
                        pizza[i][j][1] = slice_id
                mark_slice_as_processed(expandable_row_top, start_tile_column, slice_bound_bottom, slice_bound_right)
                return True

        mark_slice_as_processed(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right)
        return False

    def expand_to_left(start_tile_row, start_tile_column, slice_id):
        bounds = find_bounds_of_slice(start_tile_row, start_tile_column, slice_id)

        slice_bound_bottom = bounds[0]
        slice_bound_right = bounds[1]

        if start_tile_column >= 1 and calculate_slice_area(start_tile_row, start_tile_column,
                                                           slice_bound_bottom, slice_bound_right) < max_slice_size:

            expandable_column_left = explore_to_the_left(start_tile_row, start_tile_column,
                                                         slice_bound_bottom, slice_bound_right, slice_id)

            if type(expandable_column_left) == int:
                for i in range(expandable_column_left, start_tile_column + 1):
                    for j in range(start_tile_row, slice_bound_bottom + 1):
                        pizza[j][i][1] = slice_id

                mark_slice_as_processed(start_tile_row, expandable_column_left, slice_bound_bottom, slice_bound_right)
                return True

        mark_slice_as_processed(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right)
        return False

    def expand_to_bottom(start_tile_row, start_tile_column, slice_id):
        bounds = find_bounds_of_slice(start_tile_row, start_tile_column, slice_id)

        slice_bound_bottom = bounds[0]
        slice_bound_right = bounds[1]

        if slice_bound_bottom < rows - 1 and calculate_slice_area(start_tile_row, start_tile_column,
                                                                  slice_bound_bottom,
                                                                  slice_bound_right) < max_slice_size:

            expandable_row_bottom = explore_to_the_bottom(start_tile_row, start_tile_column,
                                                          slice_bound_bottom, slice_bound_right, slice_id)

            if type(expandable_row_bottom) == int:
                for i in range(slice_bound_bottom, expandable_row_bottom + 1):
                    for j in range(start_tile_column, slice_bound_right + 1):
                        pizza[i][j][1] = slice_id
                mark_slice_as_processed(start_tile_row, start_tile_column, expandable_row_bottom, slice_bound_right)
                return True

        mark_slice_as_processed(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right)
        return False

    def expand_to_right(start_tile_row, start_tile_column, slice_id):
        bounds = find_bounds_of_slice(start_tile_row, start_tile_column, slice_id)

        slice_bound_bottom = bounds[0]
        slice_bound_right = bounds[1]

        if slice_bound_bottom < columns - 1 and calculate_slice_area(start_tile_row, start_tile_column,
                                                                     slice_bound_bottom,
                                                                     slice_bound_right) < max_slice_size:

            expandable_column_right = explore_to_the_right(start_tile_row, start_tile_column,
                                                           slice_bound_bottom, slice_bound_right, slice_id)
            if type(expandable_column_right) == int:
                for i in range(slice_bound_right, expandable_column_right + 1):
                    for j in range(start_tile_row, slice_bound_bottom + 1):
                        pizza[j][i][1] = slice_id

                mark_slice_as_processed(start_tile_row, start_tile_column, slice_bound_bottom, expandable_column_right)
                return True

        mark_slice_as_processed(start_tile_row, start_tile_column, slice_bound_bottom, slice_bound_right)
        return False

    # Mark slice as processed after expansion
    def mark_slice_as_processed(start_tile_row, start_tile_column, end_tile_row, end_tile_column):
        for i in range(start_tile_row, end_tile_row + 1):
            for j in range(start_tile_column, end_tile_column + 1):
                pizza[i][j][2] = True

    def mark_pizza_ready():
        for i in range(0, rows):
            for j in range(0, columns):
                pizza[i][j][2] = False

    # Go piece by piece over the whole pizza and try to expand the area where applicable
    def maximize_pieces():
        for row in range(0, rows):
            for column in range(0, columns):
                if pizza[row][column][2] == False and pizza[row][column][1] != 0:
                    expand_to_left(row, column, pizza[row][column][1])

        mark_pizza_ready()

        for row in range(0, rows):
            for column in range(0, columns):
                if pizza[row][column][2] == False and pizza[row][column][1] != 0:
                    expand_to_bottom(row, column, pizza[row][column][1])

        mark_pizza_ready()

        for row in range(0, rows):
            for column in range(0, columns):
                if pizza[row][column][2] == False and pizza[row][column][1] != 0:
                    expand_to_right(row, column, pizza[row][column][1])

        mark_pizza_ready()

        for row in range(0, rows):
            for column in range(0, columns):
                if pizza[row][column][2] == False and pizza[row][column][1] != 0:
                    expand_to_top(row, column, pizza[row][column][1])

        mark_pizza_ready()

    def produce_output_dictionary():
        output_map = {}
        for i in range(0, rows):
            for j in range(0, columns):
                slice_id = pizza[i][j][1]
                if output_map.get(slice_id) is None:
                    slice_bounds = find_bounds_of_slice(i, j, slice_id)
                    output_map[slice_id] = [i, j, slice_bounds[0], slice_bounds[1]]

        if output_map.get(0) is not None:
            output_map.pop(0)
        return output_map

    def create_output(output_dictionary):
        print(len(output_dictionary))
        for key in output_dictionary:
            # print("sup")
            # print(output_dict[key][0])
            print("{} {} {} {}".format(output_dictionary[key][0], output_dictionary[key][1], output_dictionary[key][2],
                                       output_dictionary[key][3]))

    def create_output_file(output_dictionary):
        file = open("solution_d.out", "w")

        file.write(str(len(output_dictionary)) + "\n")
        for key in output_dictionary:
            file.write("{} {} {} {}".format(output_dictionary[key][0], output_dictionary[key][1], output_dictionary[key][2],
                                     output_dictionary[key][3]))
            file.write("\n")

    find_smallest_pieces()

    # for line in pizza:
    #     print(line)

    maximize_pieces()

    # print("\n")
    # for line in pizza:
    #     print(line)

    output_dict = produce_output_dictionary()
    # print(output_dict)

    # create_output(output_dict)
    # print("The number of Slices is: " + str(len(produce_output_dictionary())))

    create_output_file(output_dict)


___init___()
