# OptiKlear

**OptiKlear** is a Python library for vector operations and digital image processing.

It provides reusable implementations of image filtering, noise generation, geometric image transformations, matrix operations and vector mathematics.

The library is designed to make fundamental image-processing and mathematical operations accessible through individual Python functions.

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Package Structure](#package-structure)
- [API Reference](#api-reference)
  - [1. Convolution — conv](#1-convolution--conv)
  - [2. Nonlinear Filtering — non_linear](#2-nonlinear-filtering--non_linear)
  - [3. Noise Generation — noise_gen](#3-noise-generation--noise_gen)
  - [4. Image Transformations — mat_trans](#4-image-transformations--mat_trans)
  - [5. Matrix-Vector Operations — mat_vec](#5-matrix-vector-operations--mat_vec)
  - [6. Vector Operations — vec_operations](#6-vector-operations--vec_operations)
- [General Usage Examples](#general-usage-examples)
- [Input Requirements and Limitations](#input-requirements-and-limitations)
- [Development Roadmap](#development-roadmap)

---

## Installation

Install OptiKlear directly from PyPI:

```bash
pip install optiklear
```

To upgrade an existing installation:

```bash
pip install --upgrade optiklear
```

## Requirements

- Python 3.10 or later
- NumPy

Install NumPy separately if necessary:

```bash
pip install numpy
```

---

## Package Structure

```text
optiklear/
│
├── __init__.py
├── conv.py
├── non_linear.py
├── noise_gen.py
├── mat_trans.py
├── mat_vec.py
└── vec_operations.py
```

| Module | Description |
|---|---|
| `conv` | Spatial convolution for image filtering. |
| `non_linear` | Nonlinear image filtering using the median filter. |
| `noise_gen` | Generation of uniform, Gaussian and salt-and-pepper noise. |
| `mat_trans` | Geometric transformations applied to images. |
| `mat_vec` | Matrix-vector multiplication and 2D geometric transformations. |
| `vec_operations` | Mathematical operations involving 2D and 3D vectors. |

---

# API Reference

## 1. Convolution — `conv`

The `conv` module provides functions for performing spatial convolution on colour images.

Convolution applies a kernel (filter mask) across an image to produce a filtered output.

### `convolution(h, B)`

Performs spatial convolution using a supplied kernel and a three-channel image represented as a nested Python list.

**Syntax**

```python
convolution(h, B)
```

**Parameters**

| Parameter | Type | Description |
|---|---|---|
| `h` | Nested list | Convolution kernel. |
| `B` | Nested list | Input image containing three-channel pixels. |

**Returns**

A nested Python list containing the filtered image.

**Example**

```python
from optiklear.conv import convolution

kernel = [
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
]

image = [
    [[10, 20, 30], [20, 30, 40], [30, 40, 50]],
    [[20, 30, 40], [30, 40, 50], [40, 50, 60]],
    [[30, 40, 50], [40, 50, 60], [50, 60, 70]]
]

result = convolution(kernel, image)
```

**Notes**

- The kernel is rotated by 180 degrees as part of the convolution process.
- Zero padding is applied around the image.
- The supplied image and kernel are modified during processing.
- The implementation currently expects three-channel pixels.

### `rotate_kernel(h)`

Rotates a kernel by 180 degrees.

**Syntax**

```python
rotate_kernel(h)
```

**Parameters**

- `h`: A nested list representing the kernel.

**Returns**

The rotated kernel.

**Note:** The original kernel is modified.

### `get_kernel_mid(h)`

Calculates the midpoint indices of a kernel.

**Syntax**

```python
get_kernel_mid(h)
```

**Parameters**

- `h`: A nested list representing the kernel.

**Returns**

A tuple containing the midpoint row and column indices.

### `pad_matrix(h, B)`

Rotates the supplied kernel and applies zero padding to the image according to the kernel dimensions.

**Syntax**

```python
pad_matrix(h, B)
```

**Parameters**

- `h`: Convolution kernel.
- `B`: Input image represented as a nested list.

**Returns**

A tuple containing:

1. The rotated kernel.
2. The padded image.

**Note:** Both the kernel and image are modified.

---

## 2. Nonlinear Filtering — `non_linear`

The `non_linear` module provides nonlinear image filtering through median filtering.

Unlike linear convolution, median filtering operates by sorting the pixel values within a neighbourhood and selecting the median value.

### `med_filter(input_image, row_count, col_count)`

Applies a median filter to a three-channel image.

The function processes each colour channel independently and uses the median value of the corresponding neighbourhood to construct the output pixel.

**Syntax**

```python
med_filter(input_image, row_count, col_count)
```

**Parameters**

| Parameter | Type | Description |
|---|---|---|
| `input_image` | Nested list | Input image containing three-channel pixels. |
| `row_count` | Integer | Number of rows in the filtering window. |
| `col_count` | Integer | Number of columns in the filtering window. |

**Returns**

A nested Python list containing the filtered image.

**Example**

```python
from optiklear.non_linear import med_filter

filtered_image = med_filter(image, 3, 3)
```

**Notes**

- The filtering window determines the neighbourhood used to calculate each median.
- Zero padding is applied to the image.
- The original input image is preserved.
- Odd window dimensions are recommended.
- The implementation currently processes three-channel images.

### `pad_matrix(B, row_count, col_count)`

Applies zero padding to an image according to the specified filtering-window dimensions.

**Syntax**

```python
pad_matrix(B, row_count, col_count)
```

**Parameters**

- `B`: Input image represented as a nested list.
- `row_count`: Number of rows in the filtering window.
- `col_count`: Number of columns in the filtering window.

**Returns**

A tuple containing:

1. The padded image.
2. The total number of elements in the filtering window.

---

## 3. Noise Generation — `noise_gen`

The `noise_gen` module provides functions for introducing different types of noise into images.

It currently supports:

- Uniform noise.
- Gaussian noise.
- Salt-and-pepper noise.

### `unif_noise(image, lower, upper)`

Adds uniformly distributed random noise to an image.

The noise values are generated within the specified lower and upper limits.

**Syntax**

```python
unif_noise(image, lower, upper)
```

**Parameters**

| Parameter | Type | Description |
|---|---|---|
| `image` | NumPy array | Input image. |
| `lower` | Number | Lower limit of the uniform noise distribution. |
| `upper` | Number | Upper limit of the uniform noise distribution. |

**Returns**

The modified NumPy image array.

**Example**

```python
from optiklear.noise_gen import unif_noise

noisy_image = unif_noise(image, -20, 20)
```

**Notes**

- The original image is modified directly.
- Pixel values are clipped to the range 0–255.
- Values are rounded and converted to `uint8`.
- One random noise value is generated per pixel and applied to all its channels.

### `gauss_noise(image, std)`

Adds Gaussian-distributed random noise to an image.

The noise distribution has a mean of zero and a user-specified standard deviation.

**Syntax**

```python
gauss_noise(image, std)
```

**Parameters**

| Parameter | Type | Description |
|---|---|---|
| `image` | NumPy array | Input image. |
| `std` | Number | Standard deviation of the Gaussian noise distribution. |

**Returns**

The modified NumPy image array.

**Example**

```python
from optiklear.noise_gen import gauss_noise

noisy_image = gauss_noise(image, 10)
```

**Notes**

- The original image is modified directly.
- Pixel values are clipped to the range 0–255.
- Values are rounded and converted to `uint8`.
- One random noise value is generated per pixel and applied to all its channels.

### `salt_pepper_noise(image, prob_pepper, prob_salt)`

Introduces salt-and-pepper noise by randomly replacing selected pixels with black or white values.

**Syntax**

```python
salt_pepper_noise(image, prob_pepper, prob_salt)
```

**Parameters**

| Parameter | Type | Description |
|---|---|---|
| `image` | Image array or nested list | Input image. |
| `prob_pepper` | Number | Probability of introducing pepper noise. |
| `prob_salt` | Number | Probability of introducing salt noise. |

**Returns**

A copy of the input image containing salt-and-pepper noise.

**Example**

```python
from optiklear.noise_gen import salt_pepper_noise

noisy_image = salt_pepper_noise(image, 0.05, 0.05)
```

**Notes**

- Pepper noise replaces selected pixels with 0.
- Salt noise replaces selected pixels with 255.
- The original image is preserved.
- The probabilities should be between 0 and 1.

---

## 4. Image Transformations — `mat_trans`

The `mat_trans` module provides two-dimensional geometric transformations for colour images.

The transformations use matrix operations to calculate new pixel coordinates.

### `matmax_multiply(A, B)`

Performs matrix multiplication between two matrices.

**Syntax**

```python
matmax_multiply(A, B)
```

**Parameters**

- `A`: First matrix.
- `B`: Second matrix.

**Returns**

The resulting matrix after multiplication.

### `horizontal_shear2D(image, k)`

Applies horizontal shearing to an image.

**Syntax**

```python
horizontal_shear2D(image, k)
```

**Parameters**

- `image`: Input NumPy image array.
- `k`: Horizontal shear factor.

**Returns**

A transformed image array.

### `vertical_shear2D(image, k)`

Applies vertical shearing to an image.

**Syntax**

```python
vertical_shear2D(image, k)
```

**Parameters**

- `image`: Input NumPy image array.
- `k`: Vertical shear factor.

**Returns**

A transformed image array.

### `scale2D(image, Sx, Sy)`

Scales an image along the horizontal and vertical axes.

**Syntax**

```python
scale2D(image, Sx, Sy)
```

**Parameters**

- `image`: Input NumPy image array.
- `Sx`: Horizontal scaling factor.
- `Sy`: Vertical scaling factor.

**Returns**

A scaled image array.

### `clockwise_rotate2D(image, ang_deg)`

Rotates an image clockwise around its centre.

**Syntax**

```python
clockwise_rotate2D(image, ang_deg)
```

**Parameters**

- `image`: Input NumPy image array.
- `ang_deg`: Rotation angle in degrees.

**Returns**

A rotated image array.

### `antiClockwise_rotate2D(image, ang_deg)`

Rotates an image counterclockwise around its centre.

**Syntax**

```python
antiClockwise_rotate2D(image, ang_deg)
```

**Parameters**

- `image`: Input NumPy image array.
- `ang_deg`: Rotation angle in degrees.

**Returns**

A rotated image array.

### `flipX2D(image)`

Reflects an image horizontally, producing a left-to-right flip.

**Syntax**

```python
flipX2D(image)
```

**Parameters**

- `image`: Input NumPy image array.

**Returns**

A horizontally flipped image array.

### `flipY2D(image)`

Reflects an image vertically, producing a top-to-bottom flip.

**Syntax**

```python
flipY2D(image)
```

**Parameters**

- `image`: Input NumPy image array.

**Returns**

A vertically flipped image array.

### `translate2D(image, translation)`

Translates an image along the horizontal and vertical axes.

**Syntax**

```python
translate2D(image, translation)
```

**Parameters**

- `image`: Input NumPy image array.
- `translation`: A two-element sequence containing horizontal and vertical translation values: `[tx, ty]`.

**Returns**

A translated image array.

**Example**

```python
from optiklear.mat_trans import scale2D, clockwise_rotate2D

scaled_image = scale2D(image, 1.5, 1.5)

rotated_image = clockwise_rotate2D(
    scaled_image,
    45
)
```

**Important implementation notes**

- These functions currently expect three-dimensional NumPy image arrays with a channel dimension.
- The transformations use forward coordinate mapping.
- Unfilled output pixels are initialized to zero.
- Forward mapping can produce gaps in the transformed image.
- Scaling and rotation may change the output dimensions.

---

## 5. Matrix-Vector Operations — `mat_vec`

The `mat_vec` module provides matrix-vector multiplication and two-dimensional geometric transformations.

Unlike `mat_trans`, which transforms images, these functions operate directly on coordinate vectors.

### `matvec_multiply(A, x)`

Multiplies a matrix by a vector.

**Syntax**

```python
matvec_multiply(A, x)
```

**Parameters**

- `A`: Transformation matrix.
- `x`: Input vector.

**Returns**

The resulting vector.

### `horizontal_shear2D(u, k)`

Applies horizontal shearing to a two-dimensional vector.

**Syntax**

```python
horizontal_shear2D(u, k)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `k`: Horizontal shear factor.

**Returns**

The transformed vector.

### `vertical_shear2D(u, k)`

Applies vertical shearing to a two-dimensional vector.

**Syntax**

```python
vertical_shear2D(u, k)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `k`: Vertical shear factor.

**Returns**

The transformed vector.

### `scale2D(u, Sx, Sy)`

Scales a two-dimensional vector independently along both axes.

**Syntax**

```python
scale2D(u, Sx, Sy)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `Sx`: Horizontal scaling factor.
- `Sy`: Vertical scaling factor.

**Returns**

The scaled vector.

### `clockwise_rotate2D(u, ang_deg)`

Rotates a two-dimensional vector clockwise.

**Syntax**

```python
clockwise_rotate2D(u, ang_deg)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `ang_deg`: Rotation angle in degrees.

**Returns**

The rotated vector.

### `antiClockwise_rotate2D(u, ang_deg)`

Rotates a two-dimensional vector counterclockwise.

**Syntax**

```python
antiClockwise_rotate2D(u, ang_deg)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `ang_deg`: Rotation angle in degrees.

**Returns**

The rotated vector.

### `flipX2D(u)`

Reflects a two-dimensional vector across the Y-axis.

**Syntax**

```python
flipX2D(u)
```

**Parameters**

- `u`: Input two-dimensional vector.

**Returns**

The reflected vector.

### `flipY2D(u)`

Reflects a two-dimensional vector across the X-axis.

**Syntax**

```python
flipY2D(u)
```

**Parameters**

- `u`: Input two-dimensional vector.

**Returns**

The reflected vector.

### `translate2D(u, translation)`

Translates a two-dimensional vector by another vector.

**Syntax**

```python
translate2D(u, translation)
```

**Parameters**

- `u`: Input two-dimensional vector.
- `translation`: Translation vector containing horizontal and vertical offsets.

**Returns**

The translated vector.

**Example**

```python
from optiklear.mat_vec import (
    clockwise_rotate2D,
    scale2D,
    translate2D
)

u = [3, 4]

scaled = scale2D(u, 2, 2)

rotated = clockwise_rotate2D(scaled, 45)

translated = translate2D(rotated, [5, 2])
```

---

## 6. Vector Operations — `vec_operations`

The `vec_operations` module provides mathematical operations involving two-dimensional and three-dimensional vectors.

It includes vector arithmetic, magnitude, distance, dot product, cross product, coordinate conversion, rotation and translation.

### `add2D_multi(*vectors)`

Adds two or more two-dimensional vectors.

**Syntax**

```python
add2D_multi(*vectors)
```

**Parameters**

- `*vectors`: Two or more two-dimensional vectors.

**Returns**

A tuple containing the resulting X and Y components.

**Example**

```python
from optiklear.vec_operations import add2D_multi

result = add2D_multi(
    [2, 3],
    [4, 5],
    [1, 2]
)
```

### `vec_add2D(u, v)`

Adds two two-dimensional vectors.

**Syntax**

```python
vec_add2D(u, v)
```

**Parameters**

- `u`: First vector.
- `v`: Second vector.

**Returns**

A list containing the resulting vector.

### `vec_subtract2D(u, v)`

Subtracts the second two-dimensional vector from the first.

**Syntax**

```python
vec_subtract2D(u, v)
```

**Parameters**

- `u`: First vector.
- `v`: Second vector.

**Returns**

A list containing the resulting vector.

### `mag_v2D(v)`

Calculates the magnitude (length) of a two-dimensional vector.

**Syntax**

```python
mag_v2D(v)
```

**Parameters**

- `v`: Input two-dimensional vector.

**Returns**

The magnitude as a numerical value.

### `dis_vecs2D(u, v)`

Calculates the Euclidean distance between two two-dimensional vectors.

**Syntax**

```python
dis_vecs2D(u, v)
```

**Parameters**

- `u`: First vector.
- `v`: Second vector.

**Returns**

The distance between the vectors.

### `dot_product2D(u, v)`

Calculates the dot product of two two-dimensional vectors.

**Syntax**

```python
dot_product2D(u, v)
```

**Parameters**

- `u`: First vector.
- `v`: Second vector.

**Returns**

A scalar representing the dot product.

### `ang_vectors2D(u, v)`

Calculates the angle between two two-dimensional vectors.

**Syntax**

```python
ang_vectors2D(u, v)
```

**Parameters**

- `u`: First vector.
- `v`: Second vector.

**Returns**

The angle between the vectors in degrees.

### `scale(weight, v)`

Multiplies a vector by a scalar.

**Syntax**

```python
scale(weight, v)
```

**Parameters**

- `weight`: Scalar multiplication factor.
- `v`: Input vector.

**Returns**

A list containing the scaled vector.

### `pole_to_cart(radius, angle)`

Converts a polar coordinate into Cartesian coordinates.

**Syntax**

```python
pole_to_cart(radius, angle)
```

**Parameters**

- `radius`: Distance from the origin.
- `angle`: Angular coordinate in degrees.

**Returns**

A tuple containing the Cartesian X and Y coordinates.

### `polar_vector_to_cart(polar_vector)`

Converts a polar vector into Cartesian coordinates.

**Syntax**

```python
polar_vector_to_cart(polar_vector)
```

**Parameters**

- `polar_vector`: A two-element sequence containing magnitude and angle in radians.

**Returns**

A tuple containing the Cartesian X and Y components.

### `cart_to_pole(x, y)`

Converts Cartesian coordinates into polar coordinates.

**Syntax**

```python
cart_to_pole(x, y)
```

**Parameters**

- `x`: Cartesian X coordinate.
- `y`: Cartesian Y coordinate.

**Returns**

A tuple containing the radius and angle in radians.

### `cart_to_polar(vector)`

Converts a Cartesian vector into polar representation.

**Syntax**

```python
cart_to_polar(vector)
```

**Parameters**

- `vector`: Input Cartesian vector.

**Returns**

A tuple containing the vector magnitude and angle in radians.

### `rotate(angle, vectors)`

Rotates a collection of two-dimensional vectors by a specified angle.

**Syntax**

```python
rotate(angle, vectors)
```

**Parameters**

- `angle`: Rotation angle in radians.
- `vectors`: Collection of two-dimensional vectors.

**Returns**

A list containing the rotated vectors.

### `translate(translation, vectors)`

Translates a collection of two-dimensional vectors by a common translation vector.

**Syntax**

```python
translate(translation, vectors)
```

**Parameters**

- `translation`: Two-dimensional translation vector.
- `vectors`: Collection of two-dimensional vectors.

**Returns**

A list containing the translated vectors.

### `cross_prod(u, v)`

Calculates the cross product of two three-dimensional vectors.

**Syntax**

```python
cross_prod(u, v)
```

**Parameters**

- `u`: First three-dimensional vector.
- `v`: Second three-dimensional vector.

**Returns**

A list containing the resulting three-dimensional vector.

**Example**

```python
from optiklear.vec_operations import (
    vec_add2D,
    vec_subtract2D,
    mag_v2D,
    dot_product2D,
    cross_prod
)

u = [3, 4]
v = [2, 5]

print(vec_add2D(u, v))
print(vec_subtract2D(u, v))
print(mag_v2D(u))
print(dot_product2D(u, v))

a = [1, 2, 3]
b = [4, 5, 6]

print(cross_prod(a, b))
```

---

## General Usage Examples

Functions can be imported individually from their respective modules.

### Example 1: Vector Mathematics

```python
from optiklear.vec_operations import (
    vec_add2D,
    mag_v2D,
    ang_vectors2D
)

u = [3, 4]
v = [2, 5]

result = vec_add2D(u, v)
magnitude = mag_v2D(u)
angle = ang_vectors2D(u, v)

print("Vector addition:", result)
print("Magnitude:", magnitude)
print("Angle:", angle)
```

### Example 2: Image Noise Generation

```python
import cv2

from optiklear.noise_gen import gauss_noise

image = cv2.imread("image.jpg")

noisy_image = gauss_noise(image, 10)

cv2.imwrite("noisy_image.jpg", noisy_image)
```

### Example 3: Image Transformations

```python
import cv2

from optiklear.mat_trans import (
    scale2D,
    clockwise_rotate2D,
    flipX2D
)

image = cv2.imread("image.jpg")

scaled = scale2D(image, 1.5, 1.5)

rotated = clockwise_rotate2D(scaled, 45)

flipped = flipX2D(rotated)

cv2.imwrite("transformed_image.jpg", flipped)
```

### Example 4: Image Filtering

```python
import cv2

from optiklear.non_linear import med_filter

image = cv2.imread("image.jpg")

# Convert the NumPy image into a nested Python list.
image_list = image.tolist()

filtered_image = med_filter(image_list, 3, 3)

# Convert the result back to a NumPy array.
filtered_image = cv2.UMat(
    __import__("numpy").array(filtered_image, dtype="uint8")
)

cv2.imwrite("filtered_image.jpg", filtered_image)
```

---

## Input Requirements and Limitations

OptiKlear currently uses different input representations depending on the module.

| Module | Expected input |
|---|---|
| `conv` | Nested Python lists containing three-channel pixels. |
| `non_linear` | Nested Python lists containing three-channel pixels. |
| `noise_gen` | NumPy arrays for uniform and Gaussian noise; arrays or nested lists for salt-and-pepper noise. |
| `mat_trans` | Three-dimensional NumPy image arrays. |
| `mat_vec` | Python lists representing vectors and matrices. |
| `vec_operations` | Python lists or sequences representing vectors. |

Additional considerations:

- Image-processing functions in `conv` and `non_linear` currently operate on three-channel pixels.
- The convolution and median-filter implementations use zero padding.
- Some noise-generation functions modify the original image, while others return a copy.
- Geometric image transformations use forward mapping, which can produce unfilled pixels.
- Angular units differ between some coordinate-conversion functions. Refer to the individual function descriptions.

---

## Development Roadmap

Future versions of OptiKlear may introduce:

- Point operations.
- Edge detection.
- Additional spatial filtering techniques.
- Further geometric transformations.
- Additional mathematical and image-processing utilities.

---

## Project Links

- **PyPI:** https://pypi.org/project/optiklear/
- **GitHub:** https://github.com/Stevepurpose/Optiklear

**OptiKlear** — Mathematical operations and image processing in Python.

