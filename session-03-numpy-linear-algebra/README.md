# Session 03 — NumPy Deep Dive & Linear Algebra

## 🎯 What I Learned
- Created and inspected 1D, 2D, and 3D arrays
- Understood data types, memory usage (itemsize, nbytes) in NumPy vs Pandas
- Changed dtypes with `astype()` for memory optimization
- Accessed elements with indexing, slicing, and `[::-1]` reversal
- Created special arrays: `zeros`, `ones`, `full`, `eye`, `arange`, `linspace`
- Applied boolean masking and conditional assignment
- Understood broadcasting rules for array operations
- Performed mathematical operations: `sqrt`, `log`, `exp`, `mean`, `std`
- Used `argmin`, `argmax` for index-based results
- Padded arrays to match sizes for operations
- Reshaped arrays with `reshape(-1, ...)` and flattened with `ravel()`
- Generated random numbers: `rand` (uniform), `randn` (normal), `randint`, `choice`, `shuffle`
- Visualized uniform vs normal distributions
- Transposed matrices with `.T`
- Performed dot products (`@`) for vectors and matrices
- Explored fancy indexing and `np.ix_()` for advanced selection
- Stacked arrays: `vstack`, `hstack`
- Learned linear algebra: Norm (L1, L2), Determinant, Inverse, Eigenvalues & Eigenvectors

## 📁 Files
- `session03.py` — NumPy exercises and linear algebra
- `outputs/` — Uniform vs Normal distribution plot

## 🔑 Key Concepts Covered

| Concept | NumPy Function |
|---------|---------------|
| Array dimensions | `.ndim`, `.shape` |
| Memory | `.dtype`, `.itemsize`, `.nbytes` |
| Special arrays | `np.zeros()`, `np.ones()`, `np.eye()`, `np.full()` |
| Range arrays | `np.arange()`, `np.linspace()` |
| Masking | `array[(array > 2) & (array < 5)]` |
| Random (uniform) | `np.random.rand()` |
| Random (normal) | `np.random.randn()` |
| Random (integer) | `np.random.randint()` |
| Shuffle | `np.random.shuffle()` |
| Reshape | `.reshape(-1, 3)` |
| Flatten | `.ravel()` |
| Transpose | `.T` |
| Dot product | `a @ b` or `np.dot(a, b)` |
| Fancy indexing | `array[[0, 2, 3], [1, 2, 0]]` |
| Stacking | `np.vstack()`, `np.hstack()` |
| Padding | `np.pad()` |
| Norm | `np.linalg.norm(a, ord=1)` |
| Determinant | `np.linalg.det()` |
| Inverse | `np.linalg.inv()` |
| Eigenvalues | `np.linalg.eig()` |

## 🧠 Key Takeaways
- NumPy arrays are homogeneous — all elements share the same dtype
- `float32` saves 50% memory vs `float64` — crucial for big data
- Broadcasting works when dimensions are equal or one is 1
- `rand` gives uniform distribution (mean≈0.5), `randn` gives normal (mean≈0, std≈1)
- `@` operator is cleaner than `np.dot()` for matrix multiplication
- Determinant ≠ 0 is required for matrix inversion
- Eigenvalues and eigenvectors are fundamental for PCA and dimensionality reduction
