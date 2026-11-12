import numpy as np
from math import *




def matmax_multiply(A, B):

    C = [
        [
            sum(A[i][j] * B[j][k] for j in range(len(B)))
            for k in range(len(B[0]))
        ]
        for i in range(len(A))
    ]

    return C


# --------------------------------------------------
# HORIZONTAL SHEAR
# --------------------------------------------------

def horizontal_shear2D(image, k):

    A = [
        [1, k],
        [0, 1]
    ]

    height = image.shape[0]
    width = image.shape[1]

    new_width = width + int(abs(k) * height)
    new_height = height

    transformed_image = np.zeros(
        (new_height, new_width, image.shape[2]),
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(new_coordinate[0][0])
            new_row = int(new_coordinate[1][0])

            if 0 <= new_col < new_width and 0 <= new_row < new_height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image


# --------------------------------------------------
# VERTICAL SHEAR
# --------------------------------------------------

def vertical_shear2D(image, k):

    A = [
        [1, 0],
        [k, 1]
    ]

    height = image.shape[0]
    width = image.shape[1]

    new_width = width
    new_height = height + int(abs(k) * width)

    transformed_image = np.zeros(
        (new_height, new_width, image.shape[2]),
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(new_coordinate[0][0])
            new_row = int(new_coordinate[1][0])

            if 0 <= new_col < new_width and 0 <= new_row < new_height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image


# --------------------------------------------------
# SCALING
# --------------------------------------------------

def scale2D(image, Sx, Sy):

    A = [
        [Sx, 0],
        [0, Sy]
    ]

    height = image.shape[0]
    width = image.shape[1]

    new_width = int(width * abs(Sx))
    new_height = int(height * abs(Sy))

    transformed_image = np.zeros(
        (new_height, new_width, image.shape[2]),
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(new_coordinate[0][0])
            new_row = int(new_coordinate[1][0])

            if 0 <= new_col < new_width and 0 <= new_row < new_height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image



def clockwise_rotate2D(image, ang_deg):

    theta = radians(ang_deg)

    c = cos(theta)
    s = sin(theta)

    A = [
        [c, -s],
        [s, c]
    ]

    height = image.shape[0]
    width = image.shape[1]

    # Center of the original image
    center_col = (width - 1) / 2
    center_row = (height - 1) / 2

    # Size of the rotated image
    new_width = int(
        abs(width * c) + abs(height * s)
    )

    new_height = int(
        abs(height * c) + abs(width * s)
    )

    transformed_image = np.zeros(
        (new_height, new_width, image.shape[2]),
        dtype=image.dtype
    )

    # Center of the new image
    new_center_col = (new_width - 1) / 2
    new_center_row = (new_height - 1) / 2

    for row in range(height):

        for col in range(width):

            # Move the pixel coordinate so that
            # the image center becomes the origin
            coordinate = [
                [col - center_col],
                [row - center_row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            rotated_col = new_coordinate[0][0]
            rotated_row = new_coordinate[1][0]

            # Move the coordinate back to the image
            # and place it relative to the new image center
            new_col = int(round(rotated_col + new_center_col))
            new_row = int(round(rotated_row + new_center_row))

            if 0 <= new_col < new_width and 0 <= new_row < new_height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image


def antiClockwise_rotate2D(image, ang_deg):

    theta = radians(ang_deg)

    c = cos(theta)
    s = sin(theta)

    A = [
        [c, s],
        [-s, c]
    ]

    height = image.shape[0]
    width = image.shape[1]

    # Center of the original image
    center_col = (width - 1) / 2
    center_row = (height - 1) / 2

    # Size of the rotated image
    new_width = int(
        abs(width * c) + abs(height * s)
    )

    new_height = int(
        abs(height * c) + abs(width * s)
    )

    transformed_image = np.zeros(
        (new_height, new_width, image.shape[2]),
        dtype=image.dtype
    )

    # Center of the new image
    new_center_col = (new_width - 1) / 2
    new_center_row = (new_height - 1) / 2

    for row in range(height):

        for col in range(width):

            # Move the pixel coordinate so that
            # the image center becomes the origin
            coordinate = [
                [col - center_col],
                [row - center_row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            rotated_col = new_coordinate[0][0]
            rotated_row = new_coordinate[1][0]

            # Move the coordinate back to the image
            # and place it relative to the new image center
            new_col = int(round(rotated_col + new_center_col))
            new_row = int(round(rotated_row + new_center_row))

            if 0 <= new_col < new_width and 0 <= new_row < new_height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image



# --------------------------------------------------
# FLIP LEFT ↔ RIGHT
# Reflection about the Y-axis
# --------------------------------------------------

def flipX2D(image):

    A = [
        [-1, 0],
        [0, 1]
    ]

    height = image.shape[0]
    width = image.shape[1]

    transformed_image = np.zeros(
        image.shape,
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(
                new_coordinate[0][0] + (width - 1)
            )

            new_row = int(
                new_coordinate[1][0]
            )

            if 0 <= new_col < width and 0 <= new_row < height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image


# --------------------------------------------------
# FLIP TOP ↔ BOTTOM
# Reflection about the X-axis
# --------------------------------------------------

def flipY2D(image):

    A = [
        [1, 0],
        [0, -1]
    ]

    height = image.shape[0]
    width = image.shape[1]

    transformed_image = np.zeros(
        image.shape,
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(
                new_coordinate[0][0]
            )

            new_row = int(
                new_coordinate[1][0] + (height - 1)
            )

            if 0 <= new_col < width and 0 <= new_row < height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image



def translate2D(image, translation):

    tx = translation[0]
    ty = translation[1]

    A = [
        [1, 0],
        [0, 1]
    ]

    height = image.shape[0]
    width = image.shape[1]

    transformed_image = np.zeros(
        image.shape,
        dtype=image.dtype
    )

    for row in range(height):

        for col in range(width):

            coordinate = [
                [col],
                [row]
            ]

            new_coordinate = matmax_multiply(A, coordinate)

            new_col = int(
                new_coordinate[0][0] + tx
            )

            new_row = int(
                new_coordinate[1][0] + ty
            )

            if 0 <= new_col < width and 0 <= new_row < height:

                transformed_image[new_row, new_col] = image[row, col]

    return transformed_image



