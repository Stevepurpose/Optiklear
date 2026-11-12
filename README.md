# OptiKlear

**OptiKlear** is a Python library for mathematical operations and digital image processing.

It provides reusable functions for vector operations, matrix-vector transformations, image transformations, noise generation and spatial filtering.

## Features

Current functionality includes:

- **Convolution:** Spatial convolution for image filtering.
- **Nonlinear filtering:** Median filtering.
- **Noise generation:** Uniform, Gaussian and salt-and-pepper noise.
- **Geometric transformations:** Scaling, rotation, shearing, flipping and translation.
- **Matrix-vector operations:** Matrix multiplication and 2D vector transformations.
- **Vector operations:** Vector addition, subtraction, magnitude, distance, dot product, cross product and rotation.

## Installation

Install OptiKlear using pip:

```bash
pip install optiklear
```

**Note:** OptiKlear is currently under development. The package will be available on PyPI following its initial release.

## Requirements

- Python 3.10 or later
- NumPy

## Package Structure

| Module | Description |
|---|---|
| `conv` | Convolution operations |
| `non_linear` | Nonlinear image filtering |
| `noise_gen` | Image noise generation |
| `mat_trans` | 2D image transformations |
| `mat_vec` | Matrix-vector operations and transformations |
| `vec_operations` | Mathematical vector operations |

## Usage

Import individual functions from their respective modules.

For example, to use vector operations:

```python
from optiklear.vec_operations import vec_add2D, mag_v2D

u = [3, 4]
v = [2, 5]

result = vec_add2D(u, v)
magnitude = mag_v2D(u)

print(result)
print(magnitude)
```

To use image noise generation:

```python
from optiklear.noise_gen import gauss_noise

noisy_image = gauss_noise(image, 9)
```

The image-processing functions currently use NumPy arrays and/or Python lists according to their individual implementations. Check each function's input requirements before use.

## Development Roadmap

Planned additions for future versions include:

- Point operations
- Edge detection

## License

License information will be added before the first public release.