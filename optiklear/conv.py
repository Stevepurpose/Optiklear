import math

def rotate_kernel(h):

    for i in h:
        i.reverse()

    h.reverse()
    return h

def get_kernel_mid(h):

    h_length = len(h)

    h_mid_arr = math.floor(h_length / 2)
    mid_idx = math.floor(len(h[h_mid_arr]) / 2)

    return h_mid_arr, mid_idx

def pad_matrix(h, B):

    h = rotate_kernel(h)

    row_count = len(h)
    col_count = len(h[0])

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

    return h, B

def convolution(h, B):

    # Rotate kernel and pad B
    h, B = pad_matrix(h, B)

    # Get kernel midpoint indexes
    h_mid_arr, mid_idx = get_kernel_mid(h)

    output = []

    # Move the kernel across B
    for i in range(h_mid_arr, len(B) - h_mid_arr):

        row = []

        for j in range(mid_idx, len(B[i]) - mid_idx):

            total_B = 0
            total_G = 0 
            total_R = 0

             
            # Multiply kernel elements with B elements
            for k in range(len(h)):

                for l in range(len(h[k])):

                    pixel =  B[i - h_mid_arr + k][j - mid_idx + l]

                    total_B += pixel[0] * h[k][l]
                    total_G += pixel[1] * h[k][l]
                    total_R += pixel[2] * h[k][l]
                    

            row.append([total_B, total_G, total_R])

        output.append(row)

    return output

# Client Code
'''
result = convolution(
    [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ],
    [
        [1, 0, 1, 2, 2],
        [1, 1, 2, 2, 3],
        [1, 2, 2, 6, 3],
        [1, 1, 2, 2, 3]
    ]
)

print(result)
'''
