# Session 10 — PCA, Dimensionality Reduction & Outlier Detection

## 🎯 What I Learned
- Applied **PCA (Principal Component Analysis)** to reduce MNIST dimensions (784 → 3)
- Visualized high-dimensional data in 3D after PCA
- Computed mean and standard deviation of PCA-transformed data
- Detected **outliers** using Euclidean distance from mean (> 2× std)
- Used `euclidean_distances`, `manhattan_distances`, and `cosine_similarity`
- Compared manual outlier detection vs sklearn metrics
- Understood PCA as both dimensionality reduction AND feature extraction
- Looped through multiple classes to analyze per-class PCA projections

## 📁 Files
- `main.py` — PCA on MNIST, 3D visualization, outlier detection
- `outputs/` — 3D scatter plots and outlier visualizations

## 🔑 Key Concepts Covered

| Concept | Method/Tool | Description |
|---------|------------|-------------|
| PCA | `PCA(n_components=3)` | Reduces 784 dimensions to 3 |
| 3D Visualization | `matplotlib 3D projection` | Scatter plot of PCA components |
| Mean & Std | `np.mean()`, `np.std()` | Center and spread of data |
| Outlier Detection | Distance > 2× std | Points far from mean |
| Euclidean Distance | `euclidean_distances()` | Straight-line distance |
| Manhattan Distance | `manhattan_distances()` | City-block distance |
| Cosine Similarity | `cosine_similarity()` | Angle-based similarity |
| MNIST Dataset | `fetch_openml('mnist_784')` | 70K handwritten digits |


## 🧠 Key Takeaways
PCA compresses high-dimensional data while preserving variance

784 pixels → 3 components is a massive reduction for visualization

Outliers can be detected by measuring distance from the mean

2× standard deviation is a common threshold for outlier detection

PCA helps see patterns and clusters that are invisible in raw pixel space

Per-class PCA analysis shows how different digits cluster separately

euclidean_distances expects 2D input — reshape mean accordingly

## 🔧 Key Methods Used

```python
# PCA
pca = PCA(n_components=3)
pca_data = pca.fit_transform(images)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels)

# Outlier detection
mean = np.mean(pca_data, axis=0)
std = np.std(pca_data, axis=0)
outliers = euclidean_distances(pca_data, mean.reshape(1, -1)) > 2 * std
