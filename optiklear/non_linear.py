import copy


def pad_matrix(B, row_count, col_count):

    window_size = row_count * col_count

    side_pad = (col_count - 1) // 2
    across_pad = (row_count - 1) // 2

    # Side Padding
    for i in range(len(B)):
        for j in range(side_pad):
            B[i].append([0, 0, 0])
            B[i].insert(0, [0, 0, 0])

    # Create top/bottom padding row
    my_pad = [[0, 0, 0] for i in range(len(B[0]))]

    # Top and bottom padding
    for i in range(across_pad):
        B.insert(0, my_pad.copy())
        B.append(my_pad.copy())

    return B, window_size


def med_filter(input_image, row_count, col_count):

    # Make a copy so the original image is not modified
    image_copy = copy.deepcopy(input_image)

    # Pad the image
    B, window_size = pad_matrix(
        image_copy,
        row_count,
        col_count
    )

    output_image = []

    # Move the window across B
    for i in range(len(B) - row_count + 1):

        row = []

        for j in range(len(B[0]) - col_count + 1):

            # Lists for the three RGB channels
            red_values = []
            green_values = []
            blue_values = []

            # Extract the window
            for k in range(row_count):
                for l in range(col_count):

                    pixel = B[i + k][j + l]

                    red_values.append(pixel[0])
                    green_values.append(pixel[1])
                    blue_values.append(pixel[2])

            # Sort each channel
            red_values.sort()
            green_values.sort()
            blue_values.sort()

            # Get median of each channel
            median_red = red_values[window_size // 2]
            median_green = green_values[window_size // 2]
            median_blue = blue_values[window_size // 2]

            # Construct the output pixel
            row.append([
                median_red,
                median_green,
                median_blue
            ])

        output_image.append(row)

    return output_image